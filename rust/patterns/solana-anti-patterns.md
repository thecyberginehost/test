# Solana Program Anti-Patterns

## 1. Unchecked Account Owner
```rust
// BAD - trusts any account data
let data = try_from_slice::<MyData>(&account.data.borrow())?;

// GOOD - verify owner
if account.owner != program_id {
    return Err(ProgramError::IncorrectProgramId);
}
```

## 2. Missing Signer Check
```rust
// BAD
let authority = next_account_info(accounts)?;
// proceeds without checking authority.is_signer

// GOOD
if !authority.is_signer {
    return Err(ProgramError::MissingRequiredSignature);
}
```

## 3. Wrapping Arithmetic
```rust
// BAD - wraps in release mode
let total = balance + deposit;

// GOOD
let total = balance.checked_add(deposit)
    .ok_or(ProgramError::ArithmeticOverflow)?;
```

## 4. PDA Without Sufficient Seeds
```rust
// BAD - collision between users
let (pda, bump) = Pubkey::find_program_address(
    &[b"vault"],  // same PDA for everyone!
    program_id,
);

// GOOD
let (pda, bump) = Pubkey::find_program_address(
    &[b"vault", user_pubkey.as_ref()],
    program_id,
);
```

## 5. Not Verifying PDA
```rust
// BAD - trusts user-provided account is the correct PDA
let vault = next_account_info(accounts)?;
// user could pass any account

// GOOD - derive and verify
let expected_pda = Pubkey::create_program_address(
    &[b"vault", user.key.as_ref(), &[bump]],
    program_id,
)?;
if vault.key != &expected_pda {
    return Err(ProgramError::InvalidSeeds);
}
```

## 6. Closing Account Without Zeroing
```rust
// BAD - data persists, account can be reopened
**dest.lamports.borrow_mut() += **account.lamports.borrow();
**account.lamports.borrow_mut() = 0;
// Data still readable!

// GOOD
let mut data = account.data.borrow_mut();
data.fill(0);  // zero all data
drop(data);
**dest.lamports.borrow_mut() += **account.lamports.borrow();
**account.lamports.borrow_mut() = 0;
```

## 7. CPI to Unverified Program
```rust
// BAD - trusts user-provided program ID
let target_program = next_account_info(accounts)?;
invoke(&instruction, &[account], target_program)?;

// GOOD
if target_program.key != &spl_token::ID {
    return Err(ProgramError::IncorrectProgramId);
}
```

## 8. Same Account Passed Twice
```rust
// BAD - no check that src != dst
fn transfer(src: &AccountInfo, dst: &AccountInfo, amount: u64) {
    **src.lamports.borrow_mut() -= amount;
    **dst.lamports.borrow_mut() += amount;
    // If src == dst, lamports are created from nothing
}
```

## 9. Using Clock::get() vs Sysvar
```rust
// Both are fine in modern Solana, but:
// - Clock::get() is cheaper (no account needed)
// - Never trust a user-passed timestamp
let clock = Clock::get()?;
let now = clock.unix_timestamp;
```

## 10. Forgetting to Verify Mint
```rust
// BAD - token account could be for wrong mint
let user_token = Account::<TokenAccount>::try_from(account)?;
// Proceeds to transfer without checking user_token.mint

// GOOD (Anchor)
#[account(
    token::mint = expected_mint,
    token::authority = user,
)]
pub user_token: Account<'info, TokenAccount>,
```
