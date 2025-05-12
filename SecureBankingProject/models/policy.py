class SecurityPolicy:
    # Password policy
    MIN_PASSWORD_LENGTH = 10
    PASSWORD_COMPLEXITY_REGEX = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{10,}$"
    
    # Transaction policies
    MAX_TRANSACTION_LIMIT = 5000.00  # Limit per transaction
    DAILY_TRANSACTION_LIMIT = 15000.00  # Max total per user per day
    ALLOWED_TRANSACTION_TYPES = ["deposit", "withdrawal", "transfer"]
    
    # Fraud detection / suspicious activity
    MAX_FAILED_LOGIN_ATTEMPTS = 5
    SESSION_TIMEOUT_MINUTES = 15
    
    # Logging policy
    ENABLE_LOGGING = True
    LOG_FILE_PATH = "logs/audit_log.json"
    LOG_LEVEL = "INFO"  # Could be: DEBUG, INFO, WARNING, ERROR
    
    # Account security
    ACCOUNT_ID_LENGTH = 10
    ALLOW_SAME_ACCOUNT_TRANSFER = False