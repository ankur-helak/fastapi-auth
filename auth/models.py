from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.connection import Base

class User(Base):
    """
    Represents a user in the database with necessary fields and relationships.
    Parameters:
        - id (Integer): The primary key of the user.
        - full_name (String): The full name of the user.
        - email (String): The email address of the user, which is unique.
        - hashed_password (String): The hashed password for the user's account.
    Processing Logic:
        - The email is not only a required field, but it is also indexed to facilitate faster queries.
        - There is a one-to-many relationship between User and RefreshToken, where a user can have multiple refresh tokens.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    refresh_tokens = relationship("RefreshToken", back_populates="user", foreign_keys="[RefreshToken.user_email]")

class RefreshToken(Base):
    """
    Represents a refresh token record associated with a user in the database.
    Parameters:
        - id (Integer): The primary key, a unique identifier for the refresh token.
        - user_email (String): The email of the user to whom this token belongs, linked via a foreign key.
        - token (String): The refresh token string that is unique to each record.
        - expires_at (DateTime): The datetime at which the refresh token expires.
        - revoked (Boolean): Represents whether the refresh token has been revoked.
    Processing Logic:
        - The 'expires_at' field defaults to the current UTC time upon record creation.
        - The 'revoked' field defaults to False indicating the token is initially valid.
        - A relationship is established with the User model, indicating which user the token belongs to.
    """
    __tablename__ = 'refresh_tokens'

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, ForeignKey('users.email'))
    token = Column(String, unique=True, index=True)
    expires_at = Column(DateTime, default=lambda: datetime.utcnow())
    revoked = Column(Boolean, default=False)

    user = relationship("User", back_populates="refresh_tokens", foreign_keys=[user_email])

