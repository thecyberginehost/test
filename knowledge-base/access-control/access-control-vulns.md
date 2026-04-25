# Access Control Vulnerabilities

## 1. Missing Access Control
The #1 most common critical finding. Function lacks any auth check.

```solidity
// VULNERABLE - anyone can call
function setPrice(uint newPrice) external {
    price = newPrice;
}

// FIXED
function setPrice(uint newPrice) external onlyOwner {
    price = newPrice;
}
```

**Where to look:** Every external/public function. Especially: setters, pause/unpause, mint, burn, withdraw, upgrade, emergency functions.

## 2. Incorrect Modifier / Wrong Role
Function has access control but checks the wrong role.

```solidity
// VULNERABLE - should be onlyAdmin not onlyOperator
function withdrawFees() external onlyOperator {
    // operators shouldn't be able to withdraw
}
```

## 3. tx.origin Authentication
```solidity
// VULNERABLE - phishable via malicious contract
require(tx.origin == owner);  // attacker tricks owner into calling their contract

// SAFE
require(msg.sender == owner);
```

## 4. Unprotected Initialize Functions
Proxy patterns require `initialize()` instead of constructor. If not protected, anyone can call it and become owner.

```solidity
// VULNERABLE
function initialize(address _owner) external {
    owner = _owner;
}

// SAFE - OpenZeppelin's initializer modifier
function initialize(address _owner) external initializer {
    owner = _owner;
}
```

**Double-init:** Some implementations allow re-initialization. Check `initializer` vs `reinitializer`.

## 5. Delegatecall to Untrusted Contract
If a contract delegatecalls user-supplied address, attacker can execute arbitrary code in the contract's context.

```solidity
// VULNERABLE
function execute(address target, bytes calldata data) external {
    target.delegatecall(data);  // attacker controls target
}
```

## 6. Signature Replay
Missing nonce or chain ID in signed messages allows replaying signatures across chains or after state changes.

```solidity
// VULNERABLE - no nonce, no chainId
bytes32 hash = keccak256(abi.encodePacked(user, amount));

// SAFE
bytes32 hash = keccak256(abi.encodePacked(user, amount, nonce[user]++, block.chainid, address(this)));
```

## 7. Frontrunnable Initialization
Deployer deploys contract → attacker frontruns `initialize()` call.

**Fix:** Deploy + initialize in same tx (via factory), or use constructor.

## 8. Default Visibility
Pre-Solidity 0.8: functions defaulted to `public`. Newer versions require explicit visibility, but legacy contracts may have this.

## 9. Centralization Risks (Not Bugs, But Bounty-Worthy)
Many programs pay for centralization findings:
- Single owner can drain all funds
- No timelock on critical parameter changes
- Admin can pause withdrawals indefinitely
- Upgradeable with no multisig requirement
- Single EOA as owner (not multisig)

## Checklist
- [ ] Every external/public function has appropriate access control
- [ ] No tx.origin for auth
- [ ] initialize() protected with initializer modifier
- [ ] initialize() called in deployment tx (not separately)
- [ ] No delegatecall to user-supplied addresses
- [ ] Signatures include nonce + chainId + contract address
- [ ] Admin functions have timelocks
- [ ] Roles properly separated (admin vs operator vs keeper)
- [ ] Ownership transfer is 2-step (pending + accept)
- [ ] Constructor/initializer sets correct initial roles
