"""
Title: Secure Audit Logging Utility
Author: John A. Kibozi
Course: CSC3028X00
Date: March 10, 2025
Description:
This module handles secure audit logging for the Secure Banking System.
It logs user actions, transactions, and potential security events.
"""

import logging
from datetime import datetime
import os


# Ensure log directory exists
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure logger
logging.basicConfig(
    filename="logs/audit_log.txt",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    filemode='a'
)

def log_event(message: str, level: str = "info"):
    """Logs an event to the console with a timestamp and log level."""
    timestamp = datetime.datetime.now().isoformat()
    print(f"[{timestamp}] [{level.upper()}] {message}")
    
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    elif level == "critical":
        logging.critical(message)


print("✅ Audit logger initialized.")