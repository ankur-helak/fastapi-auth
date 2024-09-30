from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    A class that holds configuration settings for an application.
    Parameters:
        - access_token_expire_minutes (int): The expiry time in minutes for the access token.
        - refresh_token_expire_days (int): The expiry time in days for the refresh token.
        - secret_key (str): Secret key used for encoding and decoding the JWT tokens.
        - algorithm (str): Algorithm to use for JWT encoding.
        - database_url (str): Database connection URL.
    Processing Logic:
        - Default values are provided for each configuration setting.
        - Reads environment-specific settings from a '.env' file if it exists.
    """
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7
    secret_key: str = "oGZGMadkunyMgtSxgV8dFg2UWkaqxYUvopvsvK7axrm61UekefE7mQrhQLJTt37E"
    algorithm: str = "HS256"
    database_url: str = "postgresql+asyncpg://authdb_owner:0MFqZ9rjyEUX@ep-falling-dust-a1nu2soz.ap-southeast-1.aws.neon.tech/authdb"

    class Config:
        env_file = ".env"

settings = Settings()