# Audit Notes Template

## Protocol: [Name]
**Date:** [YYYY-MM-DD]
**Scope:** [Which contracts]
**Commit:** [Git hash]
**Platform:** [Immunefi / Code4rena / Sherlock]
**Bounty Range:** [$X - $Y]

## Protocol Overview
- **What it does:** [1-2 sentence summary]
- **Chain(s):** [Ethereum / BSC / Solana / etc.]
- **TVL:** [$X]
- **Token:** [Name, mechanics]
- **Dependencies:** [Chainlink, Uniswap, etc.]

## Architecture
[Contract diagram / inheritance tree / key interactions]

## Key Invariants
1. [Total deposits == total shares * share price]
2. [Only admin can upgrade]
3. [User can always withdraw their funds]
4. ...

## Token Flows
[Trace how tokens move through the protocol]

## Trust Assumptions
- Admin is trusted to: [X, Y, Z]
- Users can: [X, Y, Z]
- External protocols assumed: [not to rug, maintain liquidity, etc.]

## Attack Surface
- [ ] Flash loan interactions
- [ ] Oracle dependencies
- [ ] Cross-contract calls
- [ ] Upgrade mechanism
- [ ] Governance
- [ ] Token quirks (fee-on-transfer, rebasing)

## Findings

### [F-01] Title — Severity
**File:** `Contract.sol:L42`
**Description:**
**Impact:**
**PoC:**
**Fix:**

### [F-02] Title — Severity
...

## Time Log
| Date | Hours | Focus |
|------|-------|-------|
| | | |
| | | |
| **Total** | | |
