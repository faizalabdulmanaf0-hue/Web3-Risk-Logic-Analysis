def validate_transaction(transaction):
    """Validate transaction data before calculating the risk score."""

    if not isinstance(transaction, dict):
        raise TypeError("transaction must be a dictionary")

    required_fields = {
        "blacklisted",
        "amount",
        "contract_verified",
        "wallet_age_days",
        "failed_transactions",
    }

    missing_fields = required_fields - transaction.keys()

    if missing_fields:
        raise ValueError(
            f"Missing required fields: {', '.join(sorted(missing_fields))}"
        )

    # Boolean fields must actually be bool.
    if not isinstance(transaction["blacklisted"], bool):
        raise TypeError("blacklisted must be True or False")

    if not isinstance(transaction["contract_verified"], bool):
        raise TypeError("contract_verified must be True or False")

    # Numeric validation.
    if isinstance(transaction["amount"], bool) or not isinstance(
        transaction["amount"], (int, float)
    ):
        raise TypeError("amount must be a number")

    if isinstance(transaction["wallet_age_days"], bool) or not isinstance(
        transaction["wallet_age_days"], int
    ):
        raise TypeError("wallet_age_days must be an integer")

    if isinstance(transaction["failed_transactions"], bool) or not isinstance(
        transaction["failed_transactions"], int
    ):
        raise TypeError("failed_transactions must be an integer")

    # Values cannot be negative.
    if transaction["amount"] < 0:
        raise ValueError("amount cannot be negative")

    if transaction["wallet_age_days"] < 0:
        raise ValueError("wallet_age_days cannot be negative")

    if transaction["failed_transactions"] < 0:
        raise ValueError("failed_transactions cannot be negative")


def calculate_risk_score(transaction):
    """Calculate a risk score from 0 to 100."""

    validate_transaction(transaction)

    score = 0

    # Critical override.
    if transaction["blacklisted"]:
        return 100

    # Large transaction.
    if transaction["amount"] > 5000:
        score += 20

    # Unverified smart contract.
    if not transaction["contract_verified"]:
        score += 20

    # New wallet.
    if transaction["wallet_age_days"] < 30:
        score += 15

    # Failed transaction history.
    if transaction["failed_transactions"] >= 5:
        score += 15

    # Maximum score.
    return min(score, 100)