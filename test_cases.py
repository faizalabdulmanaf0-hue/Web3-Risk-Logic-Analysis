from risk_engine_v2 import calculate_risk_score


test_cases = [

    {
        "name": "Test 1 - Normal Transaction",
        "data": {
            "amount": 500,
            "wallet_age_days": 365,
            "failed_transactions": 0,
            "contract_verified": True,
            "blacklisted": False
        },
        "expected": 0
    },

    {
        "name": "Test 2 - Blacklisted Wallet",
        "data": {
            "amount": 100,
            "wallet_age_days": 365,
            "failed_transactions": 0,
            "contract_verified": True,
            "blacklisted": True
        },
        "expected": 100
    },

    {
        "name": "Test 3 - Large Transaction + Unverified Contract",
        "data": {
            "amount": 10000,
            "wallet_age_days": 90,
            "failed_transactions": 0,
            "contract_verified": False,
            "blacklisted": False
        },
        "expected": 40
    },

    {
        "name": "Test 4 - New Wallet + Failed Transactions",
        "data": {
            "amount": 500,
            "wallet_age_days": 10,
            "failed_transactions": 8,
            "contract_verified": True,
            "blacklisted": False
        },
        "expected": 30
    },

    {
        "name": "Test 5 - Multiple Risk Indicators",
        "data": {
            "amount": 10000,
            "wallet_age_days": 12,
            "failed_transactions": 7,
            "contract_verified": False,
            "blacklisted": False
        },
        "expected": 70
    },

    {
        "name": "Test 6 - Blacklist Override",
        "data": {
            "amount": 10000,
            "wallet_age_days": 12,
            "failed_transactions": 7,
            "contract_verified": False,
            "blacklisted": True
        },
        "expected": 100
    }
]


print("=== RISK ENGINE INTEGRITY TEST ===\n")

passed = 0
failed = 0

for test in test_cases:

    actual = calculate_risk_score(test["data"])

    if actual == test["expected"]:
        status = "PASSED"
        passed += 1
    else:
        status = "FAILED"
        failed += 1

    print(test["name"])
    print(f"Expected: {test['expected']}")
    print(f"Actual:   {actual}")
    print(f"Status:   {status}")
    print("-" * 40)


print("\n=== TEST SUMMARY ===")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Total:  {len(test_cases)}")