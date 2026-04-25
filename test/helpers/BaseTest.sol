// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Test} from "forge-std/Test.sol";

abstract contract BaseTest is Test {
    address internal constant ATTACKER = address(uint160(uint256(keccak256("attacker"))));
    address internal constant VICTIM = address(uint160(uint256(keccak256("victim"))));

    function forkBsc(uint256 blockNumber) internal returns (uint256 forkId) {
        forkId = vm.createSelectFork("bsc", blockNumber);
    }

    function forkBscLatest() internal returns (uint256 forkId) {
        forkId = vm.createSelectFork("bsc");
    }

    function makeAttacker() internal returns (address) {
        vm.label(ATTACKER, "ATTACKER");
        vm.deal(ATTACKER, 100 ether);
        return ATTACKER;
    }

    function balanceOfERC20(address token, address who) internal view returns (uint256) {
        (bool ok, bytes memory data) = token.staticcall(abi.encodeWithSignature("balanceOf(address)", who));
        require(ok && data.length >= 32, "balanceOf failed");
        return abi.decode(data, (uint256));
    }

    function assertProfit(address token, address who, uint256 startBalance, uint256 minProfit) internal {
        uint256 endBalance = balanceOfERC20(token, who);
        assertGt(endBalance, startBalance, "no profit");
        assertGe(endBalance - startBalance, minProfit, "profit below threshold");
    }
}
