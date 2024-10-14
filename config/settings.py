from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Manages configuration settings for the application.
    Parameters:
        - access_token_expire_minutes (int): Number of minutes until the access token expires.
        - refresh_token_expire_days (int): Number of days until the refresh token expires.
        - secret_key (str): Secret key used for encoding and decoding JWT tokens.
        - algorithm (str): Algorithm used to sign the JWT token.
        - database_url (str): Database connection URL string.
    Processing Logic:
        - The class inherits from BaseSettings, which might auto-load environment variables or .env file contents.
        - Default values are set for each parameter.
        - The Config nested class is used to set environment file location.
    """
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7
    secret_key: str = "oGZGMadkunyMgtSxgV8dFg2UWkaqxYUvopvsvK7axrm61UekefE7mQrhQLJTt37E"
    algorithm: str = "HS256"
    database_url: str = "postgresql+asyncpg://authdb_owner:0MFqZ9rjyEUX@ep-falling-dust-a1nu2soz.ap-southeast-1.aws.neon.tech/authdb"

    class Config:
        env_file = ".env"

settings = Settings()