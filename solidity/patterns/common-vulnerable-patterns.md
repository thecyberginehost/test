# Common Vulnerable Solidity Patterns

Quick-reference for pattern matching during manual review.

## 1. External Call Before State Update
```solidity
// RED FLAG
(bool ok,) = msg.sender.call{value: amount}("");
balance[msg.sender] -= amount;  // too late
```

## 2. Unchecked External Call Return
```solidity
// RED FLAG
token.transfer(to, amount);  // return value ignored
payable(to).send(amount);    // return value ignored
```

## 3. Spot Price as Oracle
```solidity
// RED FLAG
(uint r0, uint r1,) = pair.getReserves();
price = r1 * 1e18 / r0;  // flash-loanable
```

## 4. Missing Slippage Protection
```solidity
// RED FLAG - amountOutMin = 0
router.swapExactTokensForTokens(amountIn, 0, path, to, deadline);
```

## 5. Hardcoded Gas in Transfer
```solidity
// RED FLAG - 2300 gas may not be enough for contract recipients
payable(to).transfer(amount);
```

## 6. Block.timestamp for Randomness
```solidity
// RED FLAG
uint random = uint(keccak256(abi.encodePacked(block.timestamp, msg.sender)));
```

## 7. Unprotected Self-Destruct
```solidity
// RED FLAG
function kill() external {
    selfdestruct(payable(owner));  // is there access control?
}
```

## 8. Storage Pointer vs Memory
```solidity
// BUG: modifying memory copy, not storage
MyStruct memory s = myMapping[key];  // should be `storage`
s.value = newValue;  // doesn't persist!
```

## 9. Ether Balance Assumption
```solidity
// RED FLAG - can be broken by selfdestruct or coinbase deposits
require(address(this).balance == expectedBalance);
```

## 10. Signature Without Nonce
```solidity
// RED FLAG - replay attack
bytes32 hash = keccak256(abi.encodePacked(to, amount));
// Missing: nonce, chainid, contract address
```

## 11. Approve Race Condition
```solidity
// RED FLAG when changing existing approval
token.approve(spender, newAmount);
// Should set to 0 first, or use increaseAllowance
```

## 12. Denial of Service via Array
```solidity
// RED FLAG
for (uint i = 0; i < users.length; i++) {
    // if users[] grows unbounded, this exceeds gas limit
}
```

## 13. Phantom Function (Proxy)
```solidity
// RED FLAG in proxy context
// If proxy has function with same selector as implementation,
// proxy intercepts the call. User can never reach implementation's version.
```

## 14. Unsafe Downcast
```solidity
// RED FLAG
uint128 small = uint128(bigNumber);  // silently truncates
```

## 15. Incorrect ERC20 Decimal Handling
```solidity
// RED FLAG - assumes 18 decimals
uint value = amount * price / 1e18;
// USDC has 6 decimals, WBTC has 8
```
