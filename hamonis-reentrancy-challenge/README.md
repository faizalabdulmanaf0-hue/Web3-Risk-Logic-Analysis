# Smart Contract Withdrawal Challenge

## Difficulty

Beginner

## Category

Security

## Objective

Analyze the withdrawal mechanism of the vault and determine whether
an attacker-controlled contract can withdraw more ETH than its
recorded balance.

## Scenario

You are reviewing a decentralized ETH vault.

Users can deposit ETH and later withdraw their recorded balance.

The vault is already deployed and contains funds belonging to users.

Your task is to analyze the withdrawal logic and determine whether
the implementation contains a security flaw that can be exploited
by a malicious contract.

## Learning Objectives

By completing this challenge, you should learn how to:

- Analyze Solidity withdrawal logic.
- Identify dangerous external calls.
- Understand how attacker-controlled contracts behave.
- Reason about state changes during an external call.
- Improve withdrawal logic using secure design patterns.

## Success Criteria

Demonstrate that the vault can be made to transfer more ETH to an
attacker-controlled contract than the attacker's initial recorded
balance.

## Files

- `src/VulnerableVault.sol` — the vault implementation.
- `src/Attacker.sol` — an example attacker contract used for challenge validation.
- `test/ReentrancyChallenge.t.sol` — validation test.