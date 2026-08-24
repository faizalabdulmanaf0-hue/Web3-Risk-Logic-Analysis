// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";
import "../src/VulnerableVault.sol";
import "../src/Attacker.sol";

contract ReentrancyChallengeTest is Test {
    VulnerableVault vault;
    Attacker attacker;

    address victim = address(0xBEEF);

    function setUp() public {
        vault = new VulnerableVault();
        attacker = new Attacker(address(vault));

        vm.deal(victim, 10 ether);

        vm.prank(victim);
        vault.deposit{value: 10 ether}();
    }

    function testReentrancyDrainsVault() public {
        uint256 vaultBefore = address(vault).balance;

        attacker.attack{value: 1 ether}(1 ether, 5);

        uint256 vaultAfter = address(vault).balance;

        assertEq(vaultBefore, 10 ether);
        assertLt(vaultAfter, vaultBefore);
        assertEq(vaultAfter, 4 ether);
        assertEq(address(attacker).balance, 7 ether);
    }
}