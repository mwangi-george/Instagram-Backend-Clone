from pydantic import BaseModel, EmailStr, Field, field_validator
import re


class ActionConfirm(BaseModel):
    msg: str


class UserCreate(BaseModel):
    """ Validation Schema for creating a user """
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=8)

    @field_validator('username')
    def username_rules(cls, user_name_to_validate: str):
        # Only letters, numbers, underscores, and periods are allowed in a username
        if not re.match(pattern="^[a-zA-Z0-9._]+$", string=user_name_to_validate):
            raise ValueError("Username can only contain letters, numbers, underscores, and periods.")
        return user_name_to_validate

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "jdoe@gmail.com",
                "password": "DOE@JOHN_291",
            }
        }


class TokenData(BaseModel):
    token: str


class TokenCreate(BaseModel):
    access_token: str
    token_type: str


class PasswordResetRequest(BaseModel):
    email: EmailStr


class ChangePasswordSchema(BaseModel):
    token: str
    new_password: str = Field(..., min_length=8)
