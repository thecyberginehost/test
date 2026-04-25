# Lending Protocol Vulnerabilities

## 1. Oracle Manipulation
Most critical vector. If price feed can be manipulated → borrow more than collateral is worth → protocol insolvent.

**Vectors:**
- Spot DEX price (trivially manipulable via flash loan)
- Stale Chainlink feeds (check `updatedAt` timestamp)
- Missing circuit breakers on extreme price moves
- L2 sequencer downtime → stale prices

**Audit:** Trace every `getPrice()` call back to source. Verify staleness checks, fallbacks, deviation thresholds.

## 2. Liquidation Issues
- **Self-liquidation:** Can user liquidate themselves to extract value?
- **Liquidation race conditions:** MEV bots frontrun liquidators
- **Cascading liquidations:** Large liquidation crashes price → more liquidations (death spiral)
- **Unliquidatable positions:** Edge cases where math prevents liquidation
- **Dust positions:** Tiny positions too small to profitably liquidate

## 3. Interest Rate Manipulation
If interest rate model depends on utilization, attacker can flash-loan to manipulate utilization ratio.

## 4. Collateral Factor Exploits
- New collateral listed with too-high factor → immediately borrow max → dump collateral
- Cross-collateral interactions where correlated assets amplify risk

## 5. Bad Debt Socialization
When underwater positions are liquidated at a loss, who eats it? Check the bad debt mechanism.

## 6. Share/Exchange Rate Manipulation (ERC4626)
Same inflation attack as AMM first-depositor. Donate to vault → inflate share price → steal rounding errors.

## 7. Borrow/Repay Atomicity
Can user borrow and repay in same block to game rewards or manipulate rates?

## 8. Token-Specific Issues
- Fee-on-transfer tokens: protocol accounting mismatch
- Non-standard decimals: check all decimal conversion math
- Pausable tokens: can freeze collateral/repayment
- Blacklistable tokens (USDC/USDT): frozen user can't repay → bad debt
- Tokens with multiple addresses: double-counting collateral

## High-Value Checklist
- [ ] Oracle: TWAP or Chainlink with staleness checks
- [ ] Oracle: L2 sequencer uptime feed checked
- [ ] Oracle: Circuit breaker on >X% price deviation
- [ ] Liquidation: Can't self-liquidate for profit
- [ ] Liquidation: Dust positions handled
- [ ] Liquidation: No path to unliquidatable state
- [ ] Interest: Rate can't be flash-manipulated
- [ ] Shares: First depositor attack mitigated
- [ ] Tokens: Fee-on-transfer handled
- [ ] Tokens: Non-standard decimals safe
- [ ] Tokens: Pausable/blacklistable impact assessed
- [ ] Bad debt: Socialization mechanism reviewed
- [ ] Governance: Interest model changes can't be frontrun
