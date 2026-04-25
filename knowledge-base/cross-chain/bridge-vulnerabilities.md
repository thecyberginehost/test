# Bridge & Cross-Chain Vulnerabilities

Bridges are the highest-value targets in DeFi. Over $2B stolen from bridges.

## 1. Signature Verification Failures
Bridge validators sign messages to approve transfers. If verification is broken → unlimited minting.

**Ronin Bridge ($624M):** 5/9 validators compromised. Attacker forged withdrawals.
**Wormhole ($326M):** Solana signature verification bypassed via deprecated `solana_program::sysvar::instructions`.

## 2. Message Replay
Cross-chain message replayed on same or different chain.

**Check:**
- Nonce tracking per chain
- Source chain ID in signed message
- Destination chain ID in signed message
- Message marked as consumed after processing

## 3. Fake Deposit Proofs
Attacker submits fake proof of deposit on source chain to mint on destination.

**Nomad ($190M):** Trusted root was initialized to 0x00. Any message with proof against zero root was valid.

## 4. Relayer Manipulation
If relayer can modify message contents between chains → arbitrary execution on destination.

## 5. Optimistic Bridge Issues
Optimistic bridges assume messages are valid unless challenged within a window.
- Challenge period too short → not enough time to catch fraud
- Challenger can be censored → fraud goes through
- Watcher incentives misaligned → nobody watches

## 6. Lock/Mint Accounting
Source chain locks tokens, destination chain mints wrapped version. If accounting is off:
- Mint more than locked → inflation
- Unlock more than minted → drain source chain

## Audit Priorities for Bridges
1. Validator/relayer trust model — how many need to be compromised?
2. Message format — includes chain IDs, nonces, amounts?
3. Signature verification — standard library or custom?
4. Proof verification — Merkle proofs, ZK proofs, optimistic?
5. Rate limiting — max transfer per time window?
6. Emergency pause — can bridge be halted?
7. Upgrade mechanism — who controls it?
