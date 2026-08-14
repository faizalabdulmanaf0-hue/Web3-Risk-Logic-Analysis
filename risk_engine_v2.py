def calculate_risk_score(transaction):
    score = 0

    # Critical override
    if transaction["blacklisted"] == True:
        return 100

    # Large transaction
    if transaction["amount"] > 5000:
        score += 20

    # Unverified smart contract
    if transaction["contract_verified"] == False:
        score += 20

    # New wallet
    if transaction["wallet_age_days"] < 30:
        score += 15

    # Failed transaction history
    if transaction["failed_transactions"] >= 5:
        score += 15

    # Maximum score
    if score > 100:
        score = 100

    return score