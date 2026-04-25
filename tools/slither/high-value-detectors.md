# Slither Detectors - Prioritized for Bug Bounties

## Critical / High — Always Review These Findings
| Detector | What It Finds |
|----------|--------------|
| `reentrancy-eth` | Reentrancy with ETH transfer |
| `reentrancy-no-eth` | Reentrancy without ETH (state manipulation) |
| `arbitrary-send-erc20` | Unchecked transferFrom allowing arbitrary token theft |
| `arbitrary-send-eth` | Unchecked ETH send |
| `controlled-delegatecall` | Delegatecall to user-controlled address |
| `suicidal` | Unprotected selfdestruct |
| `unprotected-upgrade` | Missing access control on upgrade function |
| `delegatecall-loop` | Delegatecall in a loop |

## Medium — Often Leads to Real Bugs
| Detector | What It Finds |
|----------|--------------|
| `unchecked-transfer` | ERC20 transfer without return check |
| `unchecked-lowlevel` | Low-level call without return check |
| `reentrancy-benign` | Reentrancy with no direct impact (but check cross-contract) |
| `tx-origin` | tx.origin used for auth |
| `incorrect-equality` | Dangerous strict equality (e.g., `balance == 0`) |
| `locked-ether` | Contract can receive ETH but can't send it out |
| `missing-zero-check` | Missing zero address validation |
| `uninitialized-state` | State variable used before assignment |
| `uninitialized-local` | Local variable used before assignment |

## Useful Printers for Recon
```bash
# Inheritance graph
slither . --print inheritance-graph

# Function summary (external/public functions with visibility)
slither . --print function-summary

# Call graph
slither . --print call-graph

# Contract summary
slither . --print contract-summary

# Variable order (critical for proxy storage layout)
slither . --print variable-order

# Human readable summary
slither . --print human-summary
```
