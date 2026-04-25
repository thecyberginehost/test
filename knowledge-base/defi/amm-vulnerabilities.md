# AMM & DEX Vulnerabilities

## 1. Sandwich Attacks (MEV)
Frontrunner sees pending swap → buys before victim → victim's swap executes at worse price → frontrunner sells.

**Audit angle:** Check if protocol has slippage protection, deadline parameters, private mempools.

## 2. Just-In-Time (JIT) Liquidity
LP adds massive liquidity right before a large swap (captures fees), removes immediately after.

**Impact:** Dilutes existing LP fee earnings.

## 3. First Depositor / Inflation Attack
First LP depositor on a vault/pool can manipulate share price to steal from subsequent depositors.

```
1. Deposit 1 wei → get 1 share
2. Donate 1M tokens directly to vault (not via deposit)
3. Share price = 1M per share
4. Next depositor with 999K tokens gets 0 shares (rounds down)
5. Attacker withdraws everything
```

**Fix:** Virtual offset (OpenZeppelin ERC4626 uses 1e3 virtual shares), minimum initial deposit, or dead shares.

## 4. Rounding Errors in Swap Math
Integer division truncation in constant-product (x*y=k) calculations can be exploited with dust amounts.

**Audit:** Check all division operations for rounding direction. Protocol should always round in its own favor.

## 5. Imbalanced Pool Manipulation
Depositing/withdrawing single-sided can shift pool ratios. If used to manipulate prices read by other protocols → attack vector.

## 6. LP Token Pricing Vulnerabilities
If LP token price is calculated from reserves (not properly), flash loans can inflate it.

**Critical for:** Lending protocols accepting LP tokens as collateral.

## 7. Fee-on-Transfer Token Issues
Tokens that take a fee on transfer break AMM accounting. Pool receives less than expected.

```solidity
// Protocol expects to receive `amount` but gets `amount - fee`
token.transferFrom(user, pool, amount);
// Pool accounting is now wrong by `fee` amount
```

**Fix:** Check balance before/after transfer, use the delta.

## 8. Rebasing Token Issues
Tokens that change balances automatically (stETH, AMPL) break pool invariants.

## Checklist for AMM Audits
- [ ] Slippage protection on all swaps
- [ ] Deadline parameter on all user-facing tx
- [ ] First depositor attack mitigated (virtual shares or min deposit)
- [ ] Rounding always favors protocol
- [ ] Fee-on-transfer tokens handled (or explicitly excluded)
- [ ] Rebasing tokens handled (or explicitly excluded)
- [ ] LP token pricing resistant to manipulation
- [ ] Skim/sync functions can't be abused
- [ ] No sandwich-able admin functions
