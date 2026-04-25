# Aderyn Usage Guide

Aderyn is a Rust-based Solidity static analyzer. Fast, modern, good complement to Slither.

## Installation
```bash
cargo install aderyn
# OR via cyfrin installer
curl -L https://raw.githubusercontent.com/Cyfrin/aderyn/main/install.sh | bash
```

## Usage
```bash
# Run on current directory (expects Foundry project)
aderyn .

# Output to specific file
aderyn . -o report.md

# Specify root
aderyn --root ./contracts
```

## Key Detectors
| Detector | What It Finds |
|----------|--------------|
| centralization-risk | Single points of failure |
| unsafe-erc20-operation | transfer/approve without SafeERC20 |
| reentrancy | External call before state update |
| unprotected-initializer | Missing initializer modifier |
| floating-pragma | Unlocked compiler version |
| missing-zero-address-check | No zero check on address params |
| state-variable-could-be-constant | Gas optimization (skip for bounty) |
| costly-operations-in-loop | Potential DoS |
| delegatecall-in-loop | Dangerous pattern |

## Aderyn vs Slither
- **Aderyn:** Faster, easier to install (no Python), cleaner output
- **Slither:** More detectors, more mature, better printers/recon tools
- **Use both.** They catch different things.

## Custom Detectors
Aderyn supports custom detectors in Rust. For bug bounty, the built-in set is usually sufficient.
