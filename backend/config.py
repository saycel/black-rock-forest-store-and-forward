import os

# environment variables
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD") or "postgres"
POSTGRES_DB = os.environ.get("POSTGRES_DB") or "brfc"
SECRET_KEY = os.environ.get("SECRET_KEY") or "SUPERSECRET!"
HTTP_AUTHORIZATION = os.environ.get("HTTP_AUTHORIZATION") or "token"

# flask constant
DATABASE_URI = f"postgresql://postgres:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DB}"
USE_API_STUBS = True
SQLALCHEMY_ECHO = True
DEBUG = True
