# General Solidity Audit Checklist

## Pre-Audit
- [ ] Read all documentation (whitepaper, docs, README)
- [ ] Understand the protocol's purpose and token flows
- [ ] Map contract architecture (inheritance, proxies, libraries)
- [ ] Identify external dependencies (oracles, DEXes, other protocols)
- [ ] Check compiler version and optimization settings
- [ ] Check if contracts are upgradeable

## Access Control
- [ ] Every external/public function has correct access control
- [ ] No tx.origin usage for authentication
- [ ] Ownership transfer is 2-step
- [ ] initialize() has initializer modifier
- [ ] initialize() called atomically with deploy
- [ ] Admin functions have timelock where appropriate
- [ ] Role separation is correct (admin/operator/keeper)

## Reentrancy
- [ ] All external calls follow Checks-Effects-Interactions
- [ ] ReentrancyGuard on state-changing functions with external calls
- [ ] ERC721/1155 callback reentrancy considered
- [ ] Cross-contract reentrancy paths mapped
- [ ] Read-only reentrancy (view functions during callbacks)

## Arithmetic
- [ ] Solidity >=0.8.0 (or SafeMath for <0.8)
- [ ] All `unchecked {}` blocks verified safe
- [ ] All assembly math verified safe
- [ ] Type casting checked for truncation
- [ ] Division before multiplication avoided (precision loss)
- [ ] Rounding direction favors protocol

## Token Handling
- [ ] SafeERC20 used for all token operations
- [ ] Fee-on-transfer tokens handled (or explicitly excluded)
- [ ] Rebasing tokens handled (or explicitly excluded)
- [ ] Non-standard decimals handled correctly
- [ ] Return values checked on approve/transfer
- [ ] Token blacklist/pause impact assessed

## Oracle
- [ ] No spot DEX prices for critical operations
- [ ] Chainlink staleness check present
- [ ] Chainlink negative price check
- [ ] L2 sequencer uptime check (if applicable)
- [ ] Fallback oracle mechanism
- [ ] Price deviation circuit breaker

## DoS
- [ ] No unbounded loops over user-controlled arrays
- [ ] No external calls in loops that can fail and block
- [ ] Pull pattern for ETH/token distribution
- [ ] Block gas limit not reachable by normal operations
- [ ] Dust amount handling

## Logic
- [ ] All invariants documented and verified
- [ ] Edge cases: zero amounts, max amounts, empty arrays
- [ ] First and last user behavior
- [ ] Time-based logic boundaries (epoch, deadline, cooldown)
- [ ] State machine transitions all valid
- [ ] No front-runnable initialization or configuration

## Proxy / Upgrade
- [ ] Storage layout preserved between versions
- [ ] Storage gaps for future expansion
- [ ] Implementation constructor has _disableInitializers()
- [ ] UUPS upgrade function has access control
- [ ] No selfdestruct in implementation
- [ ] No immutable variables that should be in storage

## Gas & Optimization
- [ ] Gas optimizations don't introduce bugs
- [ ] Unchecked blocks truly can't overflow
- [ ] Assembly blocks are correct

## External Integrations
- [ ] All external call return values checked
- [ ] Reentrancy from external calls considered
- [ ] External protocol upgrade/pause impact assessed
- [ ] Hardcoded addresses are correct per chain

## Events & Monitoring
- [ ] Critical state changes emit events
- [ ] Events have correct indexed parameters
- [ ] No sensitive data leaked in events

## Governance / Centralization
- [ ] Admin key compromise impact assessed
- [ ] Multisig requirement for critical functions
- [ ] Timelock on parameter changes
- [ ] Emergency functions properly scoped
- [ ] Upgrade path requires governance
