# Reentrancy - All Variants

## 1. Classic Reentrancy (Single-Function)
**The OG.** External call before state update lets attacker re-enter the same function.

```solidity
// VULNERABLE
function withdraw(uint amount) external {
    require(balances[msg.sender] >= amount);
    (bool ok,) = msg.sender.call{value: amount}("");  // <-- attacker re-enters here
    require(ok);
    balances[msg.sender] -= amount;  // state updated AFTER call
}
```

**Fix:** Checks-Effects-Interactions pattern. Update state BEFORE external call.
```solidity
function withdraw(uint amount) external {
    require(balances[msg.sender] >= amount);
    balances[msg.sender] -= amount;  // state FIRST
    (bool ok,) = msg.sender.call{value: amount}("");
    require(ok);
}
```

## 2. Cross-Function Reentrancy
Attacker re-enters a DIFFERENT function that reads the stale state.

```solidity
// VULNERABLE - withdraw() calls out, attacker re-enters transfer()
function withdraw(uint amount) external {
    require(balances[msg.sender] >= amount);
    (bool ok,) = msg.sender.call{value: amount}("");
    require(ok);
    balances[msg.sender] -= amount;
}

function transfer(address to, uint amount) external {
    require(balances[msg.sender] >= amount);  // reads stale balance
    balances[msg.sender] -= amount;
    balances[to] += amount;
}
```

**Fix:** ReentrancyGuard (nonReentrant modifier) on ALL state-changing functions, or CEI everywhere.

## 3. Cross-Contract Reentrancy
Attacker re-enters a DIFFERENT contract that shares state or reads from the vulnerable one.

**Example:** Vault deposits into Strategy, Strategy calls external protocol, attacker re-enters Vault's deposit() while Strategy's balance is inflated.

**Fix:** Global reentrancy locks across integrated contracts, or careful state isolation.

## 4. Read-Only Reentrancy
Attacker exploits a VIEW function that reads inconsistent state mid-execution. No direct state modification needed — the stale read is used by another protocol.

**Real-world:** Curve pool's `get_virtual_price()` read during `remove_liquidity()` callback returns inflated value. Attacker uses this in a lending protocol that prices LP tokens via `get_virtual_price()`.

```solidity
// Curve pool (simplified)
function remove_liquidity(uint amount) external {
    // Burns LP tokens, sends ETH via callback
    // get_virtual_price() returns STALE value during callback
    _burn(msg.sender, amount);
    (bool ok,) = msg.sender.call{value: ethAmount}("");  // callback here
    // ... updates reserves AFTER callback
}
```

**Fix:** Lending protocols must use reentrancy-aware price feeds, or check pool's lock state.

## 5. ERC-721/1155 Callback Reentrancy
`onERC721Received` and `onERC1155Received` callbacks create reentrancy vectors during mints/transfers.

```solidity
// VULNERABLE NFT mint
function mint(uint quantity) external payable {
    require(totalSupply + quantity <= MAX);
    for (uint i = 0; i < quantity; i++) {
        _safeMint(msg.sender, totalSupply + i);  // calls onERC721Received
    }
}
```
Attacker's `onERC721Received` re-enters `mint()` before totalSupply is fully updated.

**Fix:** Update counters before minting, or use nonReentrant.

## 6. Governance Reentrancy
Flash-loan governance tokens → vote → re-enter during execution callback → vote again or manipulate quorum.

## Detection
- **Slither:** `reentrancy-eth`, `reentrancy-no-eth`, `reentrancy-benign`, `reentrancy-events`
- **Manual:** Search for `.call{`, `.transfer(`, `safeTransferFrom`, any external call before state update
- **Semgrep:** Pattern match external calls followed by state writes

## Severity
- Classic/Cross-function with ETH drain: **Critical**
- Read-only affecting pricing: **High**
- NFT callback mint bypass: **Medium-High**
- Events-only: **Low/Informational**
