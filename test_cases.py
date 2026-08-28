from risk_engine_v2 import calculate_risk_score


test_cases = [
    {
        "name": "Test 1 - Normal Transaction",
        "data": {
            "amount": 500,
            "wallet_age_days": 365,
            "failed_transactions": 0,
            "contract_verified": True,
            "blacklisted": False,
        },
        "expected": 0,
    },
    {
        "name": "Test 2 - Blacklisted Wallet",
        "data": {
            "amount": 100,
            "wallet_age_days": 365,
            "failed_transactions": 0,
            "contract_verified": True,
            "blacklisted": True,
        },
        "expected": 100,
    },
    {
        "name": "Test 3 - Large Transaction + Unverified Contract",
        "data": {
            "amount": 10000,
            "wallet_age_days": 90,
            "failed_transactions": 0,
            "contract_verified": False,
            "blacklisted": False,
        },
        "expected": 40,
    },
    {
        "name": "Test 4 - New Wallet + Failed Transactions",
        "data": {
            "amount": 500,
            "wallet_age_days": 10,
            "failed_transactions": 8,
            "contract_verified": True,
            "blacklisted": False,
        },
        "expected": 30,
    },
    {
        "name": "Test 5 - Multiple Risk Indicators",
        "data": {
            "amount": 10000,
            "wallet_age_days": 12,
            "failed_transactions": 7,
            "contract_verified": False,
            "blacklisted": False,
        },
        "expected": 70,
    },
    {
        "name": "Test 6 - Blacklist Override",
        "data": {
            "amount": 10000,
            "wallet_age_days": 12,
            "failed_transactions": 7,
            "contract_verified": False,
            "blacklisted": True,
        },
        "expected": 100,
    },
]


invalid_test_cases = [
    {
        "name": "Invalid 1 - Missing Field",
        "data": {
            "amount": 500,
            "wallet_age_days": 365,
            "failed_transactions": 0,
            "contract_verified": True,
        },
        "expected_error": ValueError,
    },
    {
        "name": "Invalid 2 - Amount Is String",
        "data": {
            "amount": "10000",
            "wallet_age_days": 365,
            "failed_transactions": 0,
            "contract_verified": True,
            "blacklisted": False,
        },
        "expected_error": TypeError,
    },
    {
        "name": "Invalid 3 - Blacklisted Is String",
        "data": {
            "amount": 100,
            "wallet_age_days": 365,
            "failed_transactions": 0,
            "contract_verified": True,
            "blacklisted": "False",
        },
        "expected_error": TypeError,
    },
    {
        "name": "Invalid 4 - Negative Amount",
        "data": {
            "amount": -100,
            "wallet_age_days": 365,
            "failed_transactions": 0,
            "contract_verified": True,
            "blacklisted": False,
        },
        "expected_error": ValueError,
    },
    {
        "name": "Invalid 5 - Negative Wallet Age",
        "data": {
            "amount": 100,
            "wallet_age_days": -10,
            "failed_transactions": 0,
            "contract_verified": True,
            "blacklisted": False,
        },
        "expected_error": ValueError,
    },
    {
        "name": "Invalid 6 - Negative Failed Transactions",
        "data": {
            "amount": 100,
            "wallet_age_days": 365,
            "failed_transactions": -1,
            "contract_verified": True,
            "blacklisted": False,
        },
        "expected_error": ValueError,
    },
]


print("=== RISK ENGINE TEST ===\n")

passed = 0
failed = 0

# Test normal scoring
for test in test_cases:
    try:
        actual = calculate_risk_score(test["data"])

        if actual == test["expected"]:
            print(f"PASSED: {test['name']}")
            passed += 1
        else:
            print(f"FAILED: {test['name']}")
            print(f"Expected: {test['expected']}")
            print(f"Actual:   {actual}")
            failed += 1

    except Exception as error:
        print(f"FAILED: {test['name']}")
        print(f"Unexpected error: {error}")
        failed += 1


# Test invalid input
for test in invalid_test_cases:
    try:
        calculate_risk_score(test["data"])

        print(f"FAILED: {test['name']}")
        print("Expected an error, but the input was accepted.")
        failed += 1

    except test["expected_error"]:
        print(f"PASSED: {test['name']}")
        passed += 1

    except Exception as error:
        print(f"FAILED: {test['name']}")
        print(f"Unexpected error: {type(error).__name__}: {error}")
        failed += 1


total = passed + failed

print("\n=== TEST SUMMARY ===")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Total:  {total}")