# CosmWasm (Rust) Smart Contract Vulnerabilities

## 1. Unbounded Iteration
CosmWasm has gas limits. Iterating over unbounded storage maps can exceed gas.

```rust
// VULNERABLE - if map has 100K entries, this exceeds gas
let all: Vec<_> = BALANCES
    .range(deps.storage, None, None, Order::Ascending)
    .collect::<StdResult<Vec<_>>>()?;
```

**Fix:** Pagination with `start_after` and `limit`.

## 2. Integer Overflow with Uint128/Uint256
CosmWasm's `Uint128` and `Uint256` panic on overflow in debug, but should use checked math.

```rust
// SAFE - Uint128 methods check overflow
let result = amount_a.checked_add(amount_b)?;
```

## 3. Missing Message Validation
Entry points (`execute`, `query`) must validate all fields in the message.

```rust
// VULNERABLE - no validation on amount
ExecuteMsg::Withdraw { amount } => {
    // What if amount is 0? What if it exceeds balance?
    execute_withdraw(deps, info, amount)
}
```

## 4. Incorrect Fund Handling
```rust
// VULNERABLE - doesn't check which denom was sent
let sent = info.funds[0].amount;  // panics if empty, doesn't verify denom

// SAFE
let sent = info.funds.iter()
    .find(|c| c.denom == expected_denom)
    .map(|c| c.amount)
    .unwrap_or(Uint128::zero());
```

## 5. Reply Attack
CosmWasm's `reply` entry point can be exploited if reply ID handling is incorrect or if the reply data is trusted without validation.

## 6. Storage Key Collision
If two different data types use overlapping storage prefixes, data corruption occurs.

## 7. Admin Privilege
CosmWasm contracts have an optional admin who can migrate (upgrade) the contract. Check admin is set correctly and migration is safe.

## 8. Cross-Contract Query Trust
Don't trust query results from external contracts — they can return arbitrary data.
