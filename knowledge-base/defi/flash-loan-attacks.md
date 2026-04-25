# Flash Loan Attack Patterns

## What Makes Flash Loans Dangerous
- Unlimited capital in a single transaction (atomic)
- Zero collateral required
- Enables attacks that would otherwise require millions in capital
- Combined with other vulnerabilities to amplify impact

## Common Attack Vectors

### 1. Price Oracle Manipulation
Borrow massive amount → swap on DEX to skew price → exploit protocol reading that DEX price → swap back → repay loan.

**Targets:** Any protocol using spot DEX prices (reserves ratio) as oracle.

```
Flash borrow 10M USDC
→ Swap 10M USDC → ETH on Uniswap (crashes USDC/ETH price on that pool)
→ Borrow ETH cheaply on lending protocol using manipulated price
→ Swap ETH back → USDC
→ Repay flash loan + profit
```

**Real exploits:** bZx (2020), Harvest Finance ($34M), Warp Finance ($7.7M)

### 2. Governance Manipulation
Flash borrow governance tokens → create/vote on proposal → execute in same tx if possible.

**Real exploits:** Beanstalk ($182M)

### 3. Liquidity Manipulation
Flash borrow → add/remove massive liquidity to manipulate LP token pricing → exploit.

**Real exploits:** Pancake Bunny, multiple Curve pool attacks

### 4. Reentrancy Amplification
Flash loan provides the capital needed to make a reentrancy attack profitable.

### 5. Arbitrage (Legitimate)
Not an attack per se, but flash loans power MEV arbitrage between DEXes.

## How to Audit For This

1. **Identify all external price reads** — any `getPrice()`, `getReserves()`, `get_virtual_price()`, spot calculations
2. **Check if prices can be manipulated in a single block** — if yes, vulnerable to flash loans
3. **Look for TWAP usage** — time-weighted averages resist single-block manipulation (but have their own issues with multi-block MEV)
4. **Check for same-block deposit+action restrictions** — some protocols block deposit and borrow in same block
5. **Check governance timelocks** — if proposal can be created AND executed in same tx, flash loan governance attack is possible

## Mitigations
- Use Chainlink / TWAP oracles, never spot prices
- Implement time delays between deposit and utilization
- Governance timelocks + snapshot-based voting (not live balance)
- Circuit breakers for large price deviations
