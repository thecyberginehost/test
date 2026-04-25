# Smart Contract Bug Bounty Toolkit

A comprehensive knowledge base and toolkit for smart contract security auditing and bug bounty hunting across Solidity (EVM) and Rust (Solana/Anchor) ecosystems.

## Structure

```
.
├── knowledge-base/       # Deep-dive vulnerability research & explanations
│   ├── defi/             # DeFi-specific (flash loans, AMM, lending, etc.)
│   ├── access-control/   # Auth, ownership, role-based
│   ├── reentrancy/       # All reentrancy variants
│   ├── oracle/           # Price oracle manipulation
│   ├── token/            # ERC20/721/1155 edge cases
│   ├── upgradeable/      # Proxy patterns, storage collisions
│   └── cross-chain/      # Bridge vulnerabilities
├── solidity/
│   ├── vulnerabilities/  # Categorized Solidity vulns with PoC
│   ├── patterns/         # Common vulnerable code patterns
│   └── checklists/       # Audit checklists by contract type
├── rust/
│   ├── vulnerabilities/  # Solana/Anchor-specific vulns
│   ├── patterns/         # Rust smart contract anti-patterns
│   └── checklists/       # Anchor program audit checklists
├── templates/            # Bug bounty report templates
├── tools/                # Tool configs & custom rules
│   ├── slither/          # Slither detectors & configs
│   ├── mythril/          # Mythril analysis configs
│   ├── aderyn/           # Aderyn detector configs
│   ├── semgrep/          # Custom Semgrep rules for Solidity
│   └── foundry/          # Foundry test templates for PoC
├── scripts/              # Automation scripts
└── reports/              # Your completed audit reports (gitignored)
```

## Quick Start

```bash
# Install core tools
./scripts/setup.sh

# Run automated scan on a target
./scripts/scan.sh <path-to-contracts>

# Generate report from findings
./scripts/report.sh <project-name>
```

## Workflow

1. **Recon** - Understand the protocol: docs, architecture, token flows
2. **Automated Scan** - Run Slither + Mythril + Aderyn + Semgrep
3. **Manual Review** - Use checklists, focus on business logic & DeFi interactions
4. **PoC Development** - Reproduce in Foundry fork tests
5. **Report** - Use templates, include impact + likelihood + PoC
6. **Submit** - Immunefi / Code4rena / Sherlock / Cantina

## Bug Bounty Platforms

| Platform | Focus | Payout Range |
|----------|-------|-------------|
| [Immunefi](https://immunefi.com) | DeFi protocols | $1K - $10M+ |
| [Code4rena](https://code4rena.com) | Competitive audits | $200 - $100K+ |
| [Sherlock](https://sherlock.xyz) | Contest-based | $500 - $50K+ |
| [Cantina](https://cantina.xyz) | Spearbit-backed | Varies |
| [HackerOne](https://hackerone.com) | Mixed (some web3) | Varies |
| [Hats Finance](https://hats.finance) | Decentralized | Varies |
