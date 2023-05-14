import os


# Database configuration
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
DATABASE_NAME = "atm"
DATABASE_USERNAME = "postgres"
DATABASE_PASSWORD = "password"


# Logging configuration
LOG_LEVEL = "INFO"
LOG_FILE = "atm.log"


# Other configuration
ATM_IP_ADDRESS = "127.0.0.1"
ATM_PORT = 5000


if __name__ == "__main__":
    print("ATM configuration loaded.")
