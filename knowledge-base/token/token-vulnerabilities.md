# Token Standard Vulnerabilities

## ERC20 Issues

### Approval Race Condition
`approve()` is vulnerable to frontrunning: if user changes allowance from N to M, attacker can spend N then M.

**Fix:** Use `increaseAllowance()`/`decreaseAllowance()`, or set to 0 first.

### Missing Return Value
Some tokens (USDT) don't return bool from `transfer()`/`approve()`. Code that checks return value reverts.

```solidity
// BREAKS with USDT
require(token.transfer(to, amount));

// SAFE - OpenZeppelin SafeERC20
token.safeTransfer(to, amount);
```

### Fee-on-Transfer Tokens
SAFEMOON-style tokens take fees. Protocol receives less than `amount`.

```solidity
// VULNERABLE
token.transferFrom(user, address(this), amount);
balances[user] += amount;  // WRONG - received less

// SAFE
uint before = token.balanceOf(address(this));
token.transferFrom(user, address(this), amount);
uint received = token.balanceOf(address(this)) - before;
balances[user] += received;
```

### Rebasing Tokens
Tokens like stETH, AMPL change balances automatically. Any protocol storing balance snapshots will drift.

### Double-Entry Point Tokens
Some tokens (old TUSD) have two addresses pointing to same balances. Can deposit via address A, protocol counts it, then deposit same tokens via address B.

### Tokens with >18 Decimals
Rare but exists. Overflow risk in decimal conversion math.

### Low-Decimal Tokens (USDC = 6, WBTC = 8)
Precision loss in calculations. Especially dangerous in price calculations:
```solidity
// With 6 decimal token, this loses significant precision
uint value = amount * price / 1e18;  // amount is tiny, intermediate product may truncate
```

### Pausable/Blacklistable (USDC, USDT)
- User gets blacklisted mid-position → can't repay debt → bad debt
- Token paused → protocol stuck, can't liquidate

### Weird ERC20 Behaviors Checklist
| Behavior | Examples | Impact |
|----------|----------|--------|
| No return value | USDT, BNB | Revert on transfer |
| Fee on transfer | SAFEMOON, PAXG | Accounting mismatch |
| Rebasing | stETH, AMPL | Balance drift |
| Multiple addresses | Old TUSD | Double counting |
| Blacklist | USDC, USDT | Frozen positions |
| Pausable | USDC | Frozen protocol |
| Flash-mintable | DAI | Infinite supply in 1 tx |
| Non-standard decimals | USDC(6), WBTC(8) | Precision loss |
| Callback on transfer | ERC777 | Reentrancy |
| Upgradeable | USDC | Behavior can change |

## ERC721 Issues

### Unsafe Mint/Transfer
`_mint()` doesn't call `onERC721Received`. `_safeMint()` does → reentrancy vector.

### Enumerable Assumptions
Not all ERC721 implement ERC721Enumerable. `tokenByIndex()` may not exist.

### tokenURI Manipulation
If metadata is on-chain and updateable, NFT properties can change post-sale.

## ERC1155 Issues

### Callback Reentrancy
Both `safeTransferFrom` and `safeBatchTransferFrom` call receiver hooks.

### Supply Tracking
ERC1155 doesn't have built-in totalSupply per token ID. Protocols must track manually.

## ERC4626 (Tokenized Vault) Issues

### Inflation Attack (First Depositor)
See AMM vulnerabilities. Same attack applies. OpenZeppelin mitigates with virtual shares.

### Rounding Direction
Deposits should round DOWN (user gets fewer shares). Withdrawals should round UP (user needs more shares). Both favor the vault.

```solidity
// Deposit: round down shares
shares = assets * totalSupply / totalAssets;  // implicit floor

// Withdraw: round up assets
assets = (shares * totalAssets + totalSupply - 1) / totalSupply;  // ceiling division
```
