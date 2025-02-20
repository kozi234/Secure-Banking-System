class SecurityPolicy:
    MIN_PASSWORD_LENGTH = 10
    PASSWORD_COMPLEXITY_REGEX = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{10,}$"
    MAX_TRANSACTION_LIMIT = 5000.00
