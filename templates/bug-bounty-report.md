# Bug Bounty Report Template

## Title
[Clear, descriptive title — e.g., "Reentrancy in withdraw() allows draining all pool funds"]

## Severity
[Critical / High / Medium / Low]

**Impact:** [What can an attacker achieve?]
**Likelihood:** [How easy is it to exploit? Any prerequisites?]

## Affected Contract(s)
- Contract: `ContractName.sol`
- Function(s): `withdraw()`, `_processRefund()`
- Line(s): L142-L158
- Deployed at: `0x...` (chain: Ethereum Mainnet)

## Vulnerability Description
[Clear explanation of the vulnerability. What is the root cause? Why does it exist?]

## Attack Scenario
1. Attacker deploys malicious contract with `receive()` callback
2. Attacker calls `withdraw()` with amount X
3. During ETH transfer, attacker's `receive()` re-enters `withdraw()`
4. Balance not yet updated, so second withdrawal succeeds
5. Repeat until pool is drained

## Impact
[Quantify the impact]
- Maximum extractable value: $X (based on current TVL)
- Affected users: All depositors
- Protocol impact: Complete insolvency

## Proof of Concept
```solidity
// Foundry fork test
// See attached PoC file

// To reproduce:
// 1. forge test --match-test test_PoC --fork-url <RPC> -vvvv
// 2. Expected output: attacker profit = X ETH
```

[Include full PoC code or attach as separate file]

## Recommended Fix
```solidity
// Apply Checks-Effects-Interactions pattern
function withdraw(uint amount) external nonReentrant {
    require(balances[msg.sender] >= amount, "insufficient");
    balances[msg.sender] -= amount;  // Update BEFORE call
    (bool ok,) = msg.sender.call{value: amount}("");
    require(ok, "transfer failed");
}
```

## References
- [SWC-107: Reentrancy](https://swcregistry.io/docs/SWC-107)
- [Similar exploit: Protocol X ($YM lost)](link)

---

## Submission Notes
- **Platform:** [Immunefi / Code4rena / Sherlock / etc.]
- **Program:** [Program name]
- **Submitted:** [Date]
- **Status:** [Pending / Confirmed / Paid / Disputed]
- **Bounty:** [Amount if paid]
