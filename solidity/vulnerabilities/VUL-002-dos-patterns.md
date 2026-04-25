# VUL-002: Denial of Service Patterns

**Severity:** Medium to High

## 1. Unbounded Loop Over User-Controlled Array
```solidity
// VULNERABLE - array grows with deposits, eventually exceeds gas limit
address[] public depositors;

function payAll() external {
    for (uint i = 0; i < depositors.length; i++) {
        payable(depositors[i]).transfer(amount);  // if one fails, ALL fail
    }
}
```
**Fix:** Pull pattern (users withdraw themselves), or paginated processing.

## 2. External Call Failure Blocks Function
```solidity
// VULNERABLE - if one recipient reverts, entire function fails
function distribute(address[] calldata recipients) external {
    for (uint i = 0; i < recipients.length; i++) {
        require(token.transfer(recipients[i], amount));  // one revert blocks all
    }
}
```
**Fix:** Try/catch, or skip failed transfers and log them.

## 3. Block Gas Limit DoS
If a function's gas cost grows linearly with state, attacker can make it exceed block gas limit.

**Example:** NFT with on-chain enumeration. If enumerating all tokens in a function, attacker mints thousands.

## 4. Griefing via Revert in Receive/Fallback
Contract that always reverts in `receive()` can block any function that sends it ETH.

```solidity
// Attacker contract
receive() external payable { revert(); }

// If protocol sends ETH to this contract, it always fails
```

**Fix:** Use pull pattern. Or use `call()` and handle failure gracefully.

## 5. Storage Slot DoS (Griefing)
Attacker fills mapping/array with garbage data that protocol must iterate.

## 6. Front-Running DoS
Attacker frontruns every user transaction to make it revert (e.g., manipulate price to fail slippage check).

## 7. Dust Amounts DoS
Creating thousands of tiny positions that cost more gas to process than they're worth.

## Detection
- **Slither:** `costly-loop`, `calls-loop`, `arbitrary-send-eth`
- **Manual:** Look for loops over arrays that can grow, external calls in loops
- **Key question:** "Can a user or attacker make this function exceed block gas limit?"
