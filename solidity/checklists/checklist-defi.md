# DeFi-Specific Audit Checklist

Use alongside the general checklist. This covers DeFi-specific concerns.

## AMM / DEX
- [ ] Slippage protection on all swaps
- [ ] Deadline parameter present and enforced
- [ ] First depositor / inflation attack mitigated
- [ ] LP token pricing manipulation resistant
- [ ] Fee-on-transfer token support (or explicit exclusion)
- [ ] Rounding favors pool (not user)
- [ ] Skim/sync can't be abused
- [ ] Admin functions not sandwich-able

## Lending / Borrowing
- [ ] Oracle manipulation resistant (TWAP/Chainlink, not spot)
- [ ] Liquidation can't be blocked or gamed
- [ ] Self-liquidation not profitable
- [ ] Bad debt socialization mechanism reviewed
- [ ] Interest rate can't be flash-manipulated
- [ ] Dust positions can be liquidated
- [ ] Collateral factor safe for each asset
- [ ] Borrow/supply caps enforced
- [ ] Flash loan interactions considered

## Vaults / Yield
- [ ] ERC4626 inflation attack mitigated
- [ ] Share price manipulation resistant
- [ ] Deposit/withdraw in same block restricted if needed
- [ ] Yield source risk assessed
- [ ] Harvest timing can't be gamed
- [ ] Fee calculation correct on deposit and withdraw
- [ ] Emergency withdraw works when strategy fails

## Staking / Rewards
- [ ] Reward rate change doesn't benefit/penalize existing stakers unfairly
- [ ] Precision loss in reward calculation acceptable
- [ ] Stake and unstake in same block restricted if needed
- [ ] Reward token same as stake token? (compound effects)
- [ ] Duration/epoch boundaries handled correctly
- [ ] Can't stake zero and earn rewards
- [ ] Leftover rewards handled (not stuck in contract)

## Governance
- [ ] Voting power snapshot-based (not live balance)
- [ ] Flash loan governance attack prevented
- [ ] Proposal threshold reasonable
- [ ] Timelock between vote and execution
- [ ] Emergency bypass properly gated
- [ ] Quorum can't be manipulated

## Bridges
- [ ] Message replay prevented (nonce + chain ID)
- [ ] Validator set update secure
- [ ] Rate limiting on large transfers
- [ ] Emergency pause mechanism
- [ ] Proof verification from trusted library
