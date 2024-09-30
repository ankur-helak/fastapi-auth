import os
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.future import select
from config.settings import settings
from auth.models import User, RefreshToken
from sqlalchemy.ext.asyncio import AsyncSession

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def get_password_hash(password):
    return pwd_context.hash(password)

async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Generates a JWT (JSON Web Token) with an optional expiration time.
    Parameters:
        - data (dict): Data payload to be included in the JWT.
        - expires_delta (Optional[timedelta]): The amount of time until the token expires. 
            Defaults to 15 minutes if not provided.
    Returns:
        - str: The encoded JWT as a string.
    Processing Logic:
        - The current time (UTC) is used to set the expiration time 'exp' in the payload.
        - If 'expires_delta' is not specified, a default expiration time of 15 minutes is set."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt

async def create_refresh_token(data: dict, expires_delta: timedelta, db: AsyncSession):
    """Creates a refresh token with an expiration time and additional claims.
    Parameters:
        - data (dict): The data to encode inside the token.
        - expires_delta (timedelta): The amount of time until the token expires.
        - db (AsyncSession): The database session to be used for storing refresh token.
    Returns:
        - str: The encoded JWT refresh token.
    Processing Logic:
        - The current UTC time and a unique nonce are added to the token data.
        - The token is encoded with the server's secret key and designated algorithm.
        - The refresh token is stored in the database with the user's email and expiration time."""
    expire = datetime.utcnow() + expires_delta
    nonce = os.urandom(16).hex()
    current_time = datetime.utcnow()
    extended_data = {
        **data,
        "iat": current_time,
        "nonce": nonce,
    }
    token = jwt.encode(extended_data, settings.secret_key, algorithm=settings.algorithm)
    db_refresh_token = RefreshToken(
        user_email=data["sub"],
        token=token,
        expires_at=expire,
        revoked=False
    )
    db.add(db_refresh_token)
    await db.commit()
    return token

async def authenticate_user(db, email: str, password: str):
    user = await db.execute(select(User).where(User.email == email))
    user = user.scalars().first()
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user
