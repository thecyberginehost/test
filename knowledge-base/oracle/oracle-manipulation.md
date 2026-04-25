# Oracle Manipulation

## Oracle Types & Risk Levels

| Oracle Type | Manipulation Risk | Notes |
|------------|------------------|-------|
| Spot DEX price (reserves) | **Critical** | Flash-loanable in 1 tx |
| Uniswap V3 TWAP | Medium | Multi-block MEV possible post-merge |
| Chainlink | Low | But staleness/deviation issues |
| Band Protocol | Low | Similar to Chainlink |
| Pyth (Solana) | Low | Pull-based, needs staleness check |
| Custom/DIY oracle | **Critical** | Almost always breakable |

## Spot Price Manipulation (The Classic)

Any protocol reading `getReserves()` from a Uniswap/PCS/Curve pool is vulnerable.

```solidity
// VULNERABLE - reads manipulable spot price
(uint reserve0, uint reserve1,) = pair.getReserves();
uint price = reserve1 * 1e18 / reserve0;
```

**Attack:** Flash loan → swap to skew reserves → exploit protocol → swap back → repay.

## Chainlink-Specific Issues

### Stale Price
```solidity
// VULNERABLE - no staleness check
(, int price,,,) = priceFeed.latestRoundData();

// SAFE
(uint80 roundId, int price,, uint updatedAt, uint80 answeredInRound) = priceFeed.latestRoundData();
require(price > 0, "negative price");
require(updatedAt > block.timestamp - STALENESS_THRESHOLD, "stale price");
require(answeredInRound >= roundId, "stale round");
```

### Deviation Threshold
Chainlink feeds only update when price moves >X% (deviation threshold). Between updates, price can drift up to the threshold. For a 1% deviation threshold, an attacker gets ~1% free manipulation window.

### L2 Sequencer Downtime
On Optimism/Arbitrum, if sequencer goes down, Chainlink prices freeze. When sequencer comes back up, stale prices are briefly active.

```solidity
// Must check sequencer uptime feed on L2
(, int answer, uint startedAt,,) = sequencerUptimeFeed.latestRoundData();
require(answer == 0, "sequencer down");
require(block.timestamp - startedAt > GRACE_PERIOD, "grace period");
```

## TWAP Manipulation (Post-Merge)

Pre-merge: manipulating TWAP required sustained capital across random block proposers.
Post-merge: proposers are known in advance. A validator who has 2+ consecutive blocks can manipulate TWAP.

**Practical risk:** Medium. Requires being a validator or bribing one.

## Curve get_virtual_price()

Read-only reentrancy makes `get_virtual_price()` return stale values during callbacks. Any protocol pricing Curve LP tokens via this function during a callback is vulnerable.

## Audit Checklist
- [ ] Identify ALL price feed sources
- [ ] No spot DEX prices used for critical operations
- [ ] Chainlink: staleness check present
- [ ] Chainlink: negative price check
- [ ] Chainlink: answeredInRound >= roundId
- [ ] L2: sequencer uptime feed checked with grace period
- [ ] TWAP: window long enough (>30 min)
- [ ] Fallback oracle if primary fails
- [ ] Price deviation circuit breaker
- [ ] No Curve get_virtual_price() in callback context
