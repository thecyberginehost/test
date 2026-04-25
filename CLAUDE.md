# Smart Contract Audit Toolkit - Claude Code Instructions

## Project Purpose
This is a smart contract security auditing and bug bounty hunting toolkit. It contains vulnerability knowledge, tool configs, checklists, and report templates for both Solidity (EVM) and Rust (Solana/Anchor).

## Key Conventions
- Vulnerability entries follow the format: Description, Impact, Detection, PoC, Remediation
- All Solidity PoCs use Foundry (forge test with fork mode)
- All Rust PoCs use Anchor's test framework or native solana-program-test
- Checklists are markdown with checkboxes for interactive use
- Semgrep rules follow the standard YAML format
- Slither custom detectors are Python files

## When Adding New Vulnerabilities
1. Place in the correct category directory
2. Include a working PoC or reference to one
3. Tag with severity (Critical/High/Medium/Low/Informational)
4. Include real-world exploit references where possible
5. Add detection rules to the appropriate tool config

## File Naming
- Vulnerabilities: `VUL-XXX-descriptive-name.md`
- Checklists: `checklist-<type>.md`
- Tool configs: match the tool's expected config filename
- Reports: `YYYY-MM-DD-<project-name>.md`
