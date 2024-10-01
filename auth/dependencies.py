from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from auth.schemas import TokenData
from db.connection import get_db
from config.settings import settings
from auth.models import User
from sqlalchemy.future import select

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    """Retrieves the current authenticated user from the JWT token and the database.
    Parameters:
        - token (str): The OAuth2 token used for authentication via dependency injection.
        - db (AsyncSession): The database session used to query the user information via dependency injection.
    Returns:
        - User: The user object retrieved from the database matching the email in the token data.
    Processing Logic:
        - Decodes the JWT token to extract the user email (subject of the token).
        - Validates that the extracted email is not None; otherwise, raises an HTTP 401 exception.
        - Queries the database for a user with the extracted email and fetches the first result.
        - Raises an HTTP 401 exception if the user is not found."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user_result = await db.execute(select(User).where(User.email == token_data.email))
    user = user_result.scalars().first()
    if user is None:
        raise credentials_exception
    return user
