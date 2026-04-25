# VUL-003: Business Logic Bugs

**Severity:** Varies (often Critical)

These are the highest-paying bounties. Tools can't find them — only manual review.

## 1. Wrong Comparison Operator
```solidity
// VULNERABLE: should be >= not >
require(balance > minAmount);  // fails when balance == minAmount
```

## 2. Off-By-One
```solidity
// VULNERABLE: should be < not <=
for (uint i = 0; i <= array.length; i++) {  // out of bounds on last iteration
```

## 3. Incorrect Fee Calculation
```solidity
// VULNERABLE: fee applied to wrong base
uint fee = amount * feeRate / 10000;
uint netAmount = amount - fee;
// But what if feeRate > 10000? netAmount underflows (pre-0.8)
```

## 4. State Not Reset
Flags, counters, or statuses not reset after operation completes. Allows replaying or re-entering completed flows.

## 5. Incorrect Token Amount Accounting
Protocol tracks internal balances but doesn't match actual token movements. Especially common with:
- Fee-on-transfer tokens
- Rebasing tokens
- Multi-step flows where intermediate state is wrong

## 6. Timestamp Dependence
```solidity
// Miners can manipulate block.timestamp by ~15 seconds
require(block.timestamp >= deadline);  // can be gamed
```

## 7. Incorrect Inheritance / Override
```solidity
// Child function shadows parent but has different logic
// Developer thinks parent's access control applies, but child overrode it
function transfer(address to, uint amount) public override {
    // Missing: super.transfer() or parent's checks
    _balances[msg.sender] -= amount;
    _balances[to] += amount;
}
```

## 8. Reward Distribution Errors
- Rewards calculated on stale balances
- Precision loss compounds over time
- First/last user gets disproportionate share
- Reward rate changes aren't applied retroactively when they should be (or vice versa)

## How to Find Logic Bugs
1. **Understand the protocol's invariants** — what MUST always be true?
2. **Trace token flows** — follow every token in and out
3. **Edge cases** — zero amounts, max amounts, empty arrays, first/last user
4. **State transitions** — can you reach an invalid state?
5. **Economic incentives** — can someone profit by doing something the protocol doesn't expect?
6. **Time-based logic** — what happens at boundaries (epoch changes, deadline, etc.)?

## This Is Where the Money Is
Logic bugs pay the highest bounties because:
- Automated tools can't find them
- They require deep protocol understanding
- Impact is often Critical (full fund drain)
- Each protocol has unique logic = unique bugs

Invest time understanding the protocol before hunting.
