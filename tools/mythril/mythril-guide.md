# Mythril Usage Guide for Bug Bounties

## Quick Scan
```bash
# Analyze a single file
myth analyze contracts/Target.sol --solv 0.8.20

# Deeper analysis (more execution paths, slower)
myth analyze contracts/Target.sol --execution-timeout 300 --max-depth 50

# Analyze deployed contract on-chain
myth analyze --address 0x... --rpc infura
```

## Key Mythril Detectors
| SWC ID | Name | What It Finds |
|--------|------|--------------|
| SWC-101 | Integer Overflow | Arithmetic overflow/underflow |
| SWC-104 | Unchecked Return | Ignoring return values |
| SWC-106 | Unprotected Selfdestruct | Anyone can destroy contract |
| SWC-107 | Reentrancy | State change after external call |
| SWC-110 | Assert Violation | Reachable assert (invariant broken) |
| SWC-112 | Delegatecall to Untrusted | Delegatecall to user input |
| SWC-113 | DoS with Failed Call | External call failure blocks function |
| SWC-114 | Timestamp Dependence | Logic depends on block.timestamp |
| SWC-115 | Authorization via tx.origin | tx.origin auth |
| SWC-116 | Block Timestamp Manipulation | Miner-manipulable timestamps |
| SWC-120 | Weak Randomness | Predictable randomness source |

## Mythril + Foundry
```bash
# If using Foundry, compile first then point Mythril at the source
forge build
myth analyze src/Contract.sol --solc-json remappings.json
```

## When Mythril Shines vs Slither
- **Mythril:** Better at finding reachable states (symbolic execution). Finds actual exploitable paths.
- **Slither:** Better at pattern matching, faster, more detectors. Finds potential issues.
- **Use both.** Slither for breadth, Mythril for depth on critical functions.

## Limitations
- Slow on complex contracts (minutes to hours)
- Can't reason about business logic
- Struggles with cross-contract interactions
- False positives on intentional patterns
