# Solana / Anchor Program Audit Checklist

## Account Validation
- [ ] Every account has owner check (or uses Anchor Account<>)
- [ ] Signer checks on all authority accounts
- [ ] PDA seeds are unique and include all necessary components
- [ ] PDA bump is stored and reused (not recalculated)
- [ ] No duplicate mutable accounts possible (src != dst)
- [ ] Account types can't be confused (type discriminator checked)
- [ ] All account constraints present in Anchor (#[account(...)])

## Arithmetic
- [ ] All math uses checked_add/sub/mul/div
- [ ] No silent overflow in release builds
- [ ] Precision loss in division is acceptable
- [ ] Token decimal handling correct (SPL tokens = variable decimals)

## CPI (Cross-Program Invocation)
- [ ] CPI signer seeds correct and minimal
- [ ] CPI target program ID verified (not from user input)
- [ ] CPI authority can't be escalated
- [ ] Return data from CPI validated

## Token Operations
- [ ] SPL Token program ID verified in CPI
- [ ] Token account mint matches expected mint
- [ ] Token account authority matches expected authority
- [ ] Sufficient balance checked before transfer
- [ ] Token account close returns rent to correct recipient
- [ ] Associated Token Account (ATA) used where appropriate

## Account Lifecycle
- [ ] Initialization checks prevent reinitialization
- [ ] Account closing zeroes data
- [ ] Account closing transfers all lamports
- [ ] Closed accounts can't be reopened in same tx
- [ ] Rent exemption verified

## Program Logic
- [ ] State machine transitions valid
- [ ] Time-based logic uses Clock sysvar (not passed timestamp)
- [ ] Slot-based assumptions account for variable slot times
- [ ] All instruction paths have correct error handling
- [ ] No panics/unwraps on user-controlled data

## Access Control
- [ ] Program upgrade authority secured
- [ ] Admin instructions properly gated
- [ ] Multisig for critical operations
- [ ] Authority transfer is 2-step

## Serialization
- [ ] Account discriminators prevent type confusion (Anchor default)
- [ ] Borsh deserialization handles malformed data
- [ ] Account data size sufficient for all fields
- [ ] No extra data accepted after expected fields
