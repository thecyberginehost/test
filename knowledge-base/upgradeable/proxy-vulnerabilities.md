# Upgradeable / Proxy Vulnerabilities

## Proxy Patterns Overview
| Pattern | How It Works | Risk Level |
|---------|-------------|------------|
| Transparent Proxy | Admin calls hit proxy, users hit impl | Medium |
| UUPS | Upgrade logic in implementation | High (if broken) |
| Beacon | Multiple proxies share one implementation | Medium |
| Diamond (EIP-2535) | Multiple facets per proxy | High (complexity) |
| Minimal Proxy (Clone) | Non-upgradeable cheap clones | Low |

## 1. Storage Collision
Proxy and implementation share storage. If storage layouts don't match, data corrupts.

```solidity
// Implementation V1
contract V1 {
    uint256 public value;    // slot 0
    address public owner;    // slot 1
}

// Implementation V2 - WRONG: inserted variable shifts slots
contract V2 {
    uint256 public newVar;   // slot 0 ← COLLIDES with value
    uint256 public value;    // slot 1 ← COLLIDES with owner
    address public owner;    // slot 2
}
```

**Fix:** Only append new variables. Never remove, reorder, or insert. Use storage gaps.

```solidity
contract V1 {
    uint256 public value;
    address public owner;
    uint256[48] private __gap;  // reserve 48 slots for future use
}
```

## 2. Uninitialized Implementation
Implementation contract itself is uninitialized. Attacker calls `initialize()` on implementation directly → becomes owner → `selfdestruct` (pre-Cancun) or exploits.

**Fix:** Call `_disableInitializers()` in implementation constructor.

```solidity
constructor() {
    _disableInitializers();
}
```

## 3. UUPS: Missing Upgrade Authorization
UUPS puts `upgradeTo()` in the implementation. If new implementation forgets to include it → bricked (can never upgrade again). If authorization is missing → anyone can upgrade.

```solidity
// VULNERABLE - no auth check
function upgradeTo(address newImpl) external {
    _upgradeTo(newImpl);
}

// SAFE
function upgradeTo(address newImpl) external onlyOwner {
    _upgradeTo(newImpl);
}
```

## 4. Function Selector Clashing
Proxy forwards calls based on selector (first 4 bytes of keccak256). If proxy admin function has same selector as implementation function → proxy intercepts it.

**Real case:** Transparent proxy pattern exists specifically to solve this. Admin calls always hit proxy, user calls always hit implementation.

## 5. Delegatecall + selfdestruct (Pre-Cancun)
If implementation has selfdestruct and attacker can trigger it → proxy is bricked (implementation code gone).

Post-Cancun (EIP-6780): selfdestruct only works in the same tx as creation. Still check for legacy chains.

## 6. Immutable Variables in Proxied Contracts
`immutable` vars are stored in bytecode, not storage. They're set in the implementation's bytecode, not the proxy's storage. Can cause unexpected behavior.

## 7. Constructor vs Initializer
Constructors run on the implementation contract, NOT the proxy. Any state set in constructor only exists on the implementation.

**Fix:** Always use `initialize()` for proxy patterns. Never set state in constructor (except `_disableInitializers()`).

## 8. Diamond Proxy Specific
- Facet function selector collision across facets
- Storage namespace collision between facets
- Upgrade can orphan storage if facet is removed
- Complex access control across facets

## Audit Checklist
- [ ] Storage layout preserved between versions (no reorder/insert/remove)
- [ ] Storage gaps present for future expansion
- [ ] Implementation has _disableInitializers() in constructor
- [ ] Initialize can only be called once (initializer modifier)
- [ ] UUPS: upgradeTo has proper access control
- [ ] UUPS: new implementation includes upgrade function
- [ ] No selfdestruct in implementation (or any delegatecall target)
- [ ] No immutable variables that should be in storage
- [ ] No constructor state that should be in initializer
- [ ] Function selectors don't clash between proxy and implementation
- [ ] Admin functions properly separated from user functions
