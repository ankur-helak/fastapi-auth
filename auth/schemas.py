from pydantic import BaseModel, EmailStr, field_validator 
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    """
    Represents a user creation data schema with validation.
    Parameters:
        - email (EmailStr): The email address of the user.
        - full_name (Optional[str]): The full name of the user. Defaults to None.
        - password (str): The password for the user account.
    Processing Logic:
        - The password validation checks for a minimum length of 8 characters and the inclusion of different character types.
        - Raises specific ValueErrors when the password fails to meet the security criteria.
    """
    email: EmailStr
    full_name: Optional[str] = None
    password: str

    @field_validator('password')
    def validate_password(cls, v):
        """Validates if the password meets certain security criteria.
        Parameters:
            - v (str): The password string to be validated.
        Returns:
            - str: The valid password that meets all the criteria.
        Processing Logic:
            - The function uses regular expressions to check for the presence of at least one lowercase letter, one uppercase letter, one digit, and one special character.
            - It raises specific ValueErrors for different criteria that the password fails to meet."""
        import re
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        if not re.findall('[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter.')
        if not re.findall('[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter.')
        if not re.findall('[0-9]', v):
            raise ValueError('Password must contain at least one digit.')
        if not re.findall('[^a-zA-Z0-9]', v):
            raise ValueError('Password must contain at least one special character (e.g., !, @, #, $).')
        return v

class UserRead(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    email: str
