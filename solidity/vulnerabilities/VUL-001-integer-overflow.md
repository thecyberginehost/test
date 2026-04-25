# VUL-001: Integer Overflow / Underflow

**Severity:** High (pre-0.8.0) / Low (post-0.8.0 unless unchecked)

## Description
Pre-Solidity 0.8.0: arithmetic silently wraps. `uint256(0) - 1 = type(uint256).max`.
Post-0.8.0: reverts on overflow by default, BUT `unchecked {}` blocks re-enable wrapping.

## Where to Look
- Any `unchecked {}` block — these exist for gas optimization but reintroduce overflow risk
- Assembly (`add`, `mul`, `sub` in Yul) — no overflow protection
- Inline assembly math
- Contracts compiled with Solidity <0.8.0
- Libraries that use unchecked math (some are intentional, verify)

## Dangerous Patterns

```solidity
// Pre-0.8: silent underflow
uint balance = 0;
balance -= 1;  // = 2^256 - 1

// Post-0.8: unchecked reintroduces the risk
unchecked {
    uint a = 0;
    a--;  // wraps to max uint256
}

// Yul/assembly: no protection
assembly {
    let result := add(a, b)  // can overflow silently
}
```

## Type Casting Truncation
```solidity
uint256 big = 2**200;
uint128 small = uint128(big);  // silently truncated to lower 128 bits
```

## Real Exploits
- **BEC Token (2018):** `batchTransfer` overflow allowed minting billions of tokens
- **Numerous pre-0.8 tokens** with overflow in `transfer()` math

## Detection
- **Slither:** `unchecked-transfer`, `tautology` detectors
- **Semgrep:** Match `unchecked` blocks with arithmetic
- **Manual:** Review all `unchecked {}` blocks and assembly math

## Remediation
- Use Solidity >=0.8.0
- Audit every `unchecked {}` block — verify overflow is truly impossible
- Use SafeMath for <0.8.0 contracts
- Validate cast inputs: `require(value <= type(uint128).max)`
