""" Application Settings Module
"""
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection_string(asyncMode: bool = False) -> str:
    """Get the connection string for the database

    Returns:
        string: The connection string
    """
    engine = os.environ.get("DB_ENGINE") if not asyncMode else os.environ.get("ASYNC_DB_ENGINE")
    dbhost = os.environ.get("DB_HOST")
    username = os.environ.get("DB_USERNAME")
    password = os.environ.get("DB_PASSWORD")
    dbname = os.environ.get("DB_NAME")
    return f"{engine}://{username}:{password}@{dbhost}/{dbname}"

# Database Setting
SQLALCHEMY_DATABASE_URL = get_connection_string()
SQLALCHEMY_DATABASE_URL_ASYNC = get_connection_string(asyncMode=True)

ADMIN_DEFAULT_PASSWORD = os.environ.get("DEFAULT_PASSWORD")

# JWT Setting
JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")

# API Service Security Setting
COGNITO = {
    "ENABLED": os.environ.get("COGNITO_ENABLED") == 'true',
    "HOST": os.environ.get("COGNITO_HOST"),
    "CLIENT_ID": os.environ.get("COGNITO_CLIENT_ID"),
    "CLIENT_SECRET": os.environ.get("COGNITO_CLIENT_SECRET"),
    "JWKS_URL": os.environ.get("COGNITO_JWKS_URL"),
}