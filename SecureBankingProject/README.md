# Secure-Banking-System

A secure, modular banking system implementing user authentication, encrypted transactions, logging, role-based access control, and audit trail capabilities using Python and Flask. Designed for educational and prototyping purposes with a focus on software security best practices.

---

# SecureBankingSystem

A secure, modular banking system implementing user authentication, encrypted transactions, logging, role-based access control, and audit trail capabilities using Python and Flask. Designed for educational and prototyping purposes with a focus on software security best practices.

---

SecureBankingProject 
Nane: John A. Kibozi
Course: CSC3028
Date: Mayb 2025
Assignment: Phase 4
Group: #5

🧩1. Final System Integration

Encryption Implemented:
- Data at rest** secured via `.env` keys and hashed fields
- Data in transit** prepared for TLS via Flask routing
- Environment variables configured:
  - `SECRET_KEY`
  - `DATABASE_URL`
  - `DEBUG`

Security Features:
- Password hashing with **bcrypt**
- Pydantic model validations on all input fields
- Placeholder logic for role-based access control (RBAC)
- `.env` support across both root and `/SecureBankingProject` folders

---

2. Unit Testing Summary

All test cases are passing:

```bash
pytest tests/
=========================== 11 passed in 1.46s ============================

Tests Executed:
•	✅ test_user.py: password security, validation
•	✅ test_transaction.py: schema correctness, logic integrity
•	✅ test_account.py: account validation, edge handling

3. Final Project Structure
SecureBankingProject/
├── models/
│   ├── account.py
│   ├── transaction.py
│   └── user.py
├── tests/
│   ├── test_account.py
│   ├── test_transaction.py
│   └── test_user.py
├── logs/
│   ├── audit_log.txt
│   └── audit_log.py
├── .env
└── README.md

4. Deployment Guide
# Clone the project
git clone https://github.com/kozi234/Secure-Banking-System.git
cd Secure-Banking-System

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify .env file is present in root and project subfolder
# Run all tests
pytest tests/

5. Maintenance Guide
•	Rotate secrets and passwords periodically in .env
•	Reinstall packages using pip install -r requirements.txt when switching environments
•	Run pytest after making model or schema updates
•	Avoid committing .env unless it’s scrubbed and approved
•	Maintain audit logs and test reports under /logs

6. Final Push & Commit Summary
git add .
git commit -m "Test: All unit tests passing for Phase 4 final submission"
git push origin main
Last successful push:
✔️ Branch: main
✔️ Commit: 5d9e415
✔️ Status: Synced and complete