# Solana / Anchor Program Vulnerabilities

## 1. Missing Owner Check
Not verifying account owner matches expected program. Attacker passes account owned by their program with crafted data.

```rust
// VULNERABLE - no owner check
let user_account = next_account_info(accounts)?;
let data = UserData::try_from_slice(&user_account.data.borrow())?;
// Attacker can pass any account with matching data layout

// SAFE - Anchor does this automatically with Account<>
#[account]
pub struct UserData { ... }
```

**Anchor auto-check:** `Account<'info, T>` verifies owner = program ID. Raw Solana programs must check manually.

## 2. Missing Signer Check
Not verifying that an account actually signed the transaction.

```rust
// VULNERABLE
let authority = next_account_info(accounts)?;
// Anyone can pass any pubkey as authority

// SAFE
require!(authority.is_signer, ProgramError::MissingRequiredSignature);
```

**Anchor:** Use `Signer<'info>` type or `#[account(signer)]`.

## 3. Account Confusion / Type Confusion
Accounts passed in wrong order or wrong type. Program trusts account at position N is what it expects.

```rust
// VULNERABLE - user could swap token_a_vault and token_b_vault
let token_a_vault = next_account_info(accounts)?;
let token_b_vault = next_account_info(accounts)?;
```

**Fix:** Use seeds/PDA derivation to verify accounts are correct.
```rust
#[account(
    seeds = [b"vault", token_a_mint.key().as_ref()],
    bump
)]
pub token_a_vault: Account<'info, TokenAccount>,
```

## 4. Arithmetic Overflow/Underflow
Rust release builds don't panic on overflow (they wrap). Solana programs compiled in release mode.

```rust
// VULNERABLE in release builds - wraps silently
let result = a + b;

// SAFE
let result = a.checked_add(b).ok_or(ProgramError::ArithmeticOverflow)?;
```

**Always use:** `checked_add`, `checked_sub`, `checked_mul`, `checked_div`.

## 5. PDA Seed Collision
If PDA seeds aren't unique enough, different logical accounts can derive to the same address.

```rust
// VULNERABLE - two users with same "name" get same PDA
seeds = [b"user", name.as_bytes()]

// SAFE - include user pubkey
seeds = [b"user", user.key().as_ref(), name.as_bytes()]
```

## 6. Closing Account Without Zeroing Data
When closing an account, if data isn't zeroed, it can be reopened and deserialized with stale data.

```rust
// Must zero data AND transfer lamports
**account.try_borrow_mut_data()? = &mut [];  // Not enough!
// Must also set data to all zeros
account.data.borrow_mut().fill(0);
**dest.try_borrow_mut_lamports()? += **account.try_borrow_lamports()?;
**account.try_borrow_mut_lamports()? = 0;
```

**Anchor:** `#[account(close = destination)]` handles this.

## 7. Missing Rent Exemption Check
Account not rent-exempt can be garbage-collected by the runtime.

## 8. CPI (Cross-Program Invocation) Privilege Escalation
If program A CPIs into program B with signer seeds, make sure program A can't be tricked into signing for unintended operations.

## 9. Duplicate Mutable Accounts
Passing the same account twice when program expects two different mutable accounts. Can violate invariants.

```rust
// If user passes same account for both src and dst
transfer(src, dst, amount);  // src and dst are same account = free money
```

**Anchor:** Add `constraint = src.key() != dst.key()`.

## 10. Reinitialization
Account already initialized can be re-initialized, overwriting data.

**Anchor:** `init` constraint only allows creation. Use `#[account(init, ...)]` not manual initialization.

## Detection
- **Soteria** (Solana static analyzer, now discontinued but patterns still relevant)
- **cargo-audit** for dependency vulnerabilities
- **Manual review** with Anchor IDL as guide
- **Trident** fuzzer for Anchor programs
