// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";

// ===== PoC Template for Bug Bounty Submissions =====
// 1. Fork mainnet at the block BEFORE the vulnerable state
// 2. Set up attacker contract if needed
// 3. Execute the attack
// 4. Assert profit / broken invariant

interface ITarget {
    // Add target contract interface functions here
}

interface IERC20 {
    function balanceOf(address) external view returns (uint256);
    function transfer(address, uint256) external returns (bool);
    function approve(address, uint256) external returns (bool);
}

contract AttackerContract {
    // If your PoC needs a malicious contract (e.g., for reentrancy callbacks)
    address public owner;
    ITarget public target;

    constructor(address _target) {
        owner = msg.sender;
        target = ITarget(_target);
    }

    // Example: reentrancy callback
    receive() external payable {
        // Re-enter target here if demonstrating reentrancy
    }

    // Example: ERC721 callback for mint reentrancy
    function onERC721Received(address, address, uint256, bytes calldata) external returns (bytes4) {
        // Re-enter target here
        return this.onERC721Received.selector;
    }
}

contract PoCTest is Test {
    // === CONFIGURATION ===
    // Target contract addresses (mainnet)
    address constant TARGET = address(0); // TODO: set target contract
    address constant TOKEN = address(0);  // TODO: set token if needed

    // Fork block - set to block BEFORE the vulnerable state
    uint256 constant FORK_BLOCK = 0; // TODO: set block number

    // Actors
    address attacker = makeAddr("attacker");

    ITarget target;
    AttackerContract attackerContract;

    function setUp() public {
        // Fork mainnet
        // vm.createSelectFork("mainnet", FORK_BLOCK);
        // OR for BSC:
        // vm.createSelectFork("bsc", FORK_BLOCK);

        target = ITarget(TARGET);

        // Fund attacker if needed
        vm.deal(attacker, 10 ether);

        // Deploy attacker contract if needed
        vm.prank(attacker);
        attackerContract = new AttackerContract(TARGET);
    }

    function test_PoC() public {
        // === BEFORE STATE ===
        // Log initial balances / state
        uint256 attackerBalanceBefore = attacker.balance;
        emit log_named_uint("Attacker ETH before", attackerBalanceBefore);

        // === ATTACK ===
        vm.startPrank(attacker);

        // TODO: Execute attack steps here
        // Step 1: ...
        // Step 2: ...
        // Step 3: ...

        vm.stopPrank();

        // === AFTER STATE ===
        uint256 attackerBalanceAfter = attacker.balance;
        emit log_named_uint("Attacker ETH after", attackerBalanceAfter);

        // === ASSERTIONS ===
        // Prove the vulnerability
        assertGt(attackerBalanceAfter, attackerBalanceBefore, "Attacker should profit");

        // Log profit
        emit log_named_uint("Profit", attackerBalanceAfter - attackerBalanceBefore);
    }
}

// Run with:
// forge test --match-test test_PoC -vvvv --fork-url <RPC_URL> --fork-block-number <BLOCK>
