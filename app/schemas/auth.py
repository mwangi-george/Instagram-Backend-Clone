from pydantic import BaseModel, EmailStr, Field, field_validator
import re
import phonenumbers


class ActionConfirm(BaseModel):
    msg: str


class UserCreate(BaseModel):
    """ Validation Schema for creating a user """
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    mobile_number: str | None = None
    password: str = Field(..., min_length=8)

    @field_validator('username')
    def username_rules(cls, user_name_to_validate: str):
        # Only letters, numbers, underscores, and periods are allowed in a username
        if not re.match(pattern="^[a-zA-Z0-9._]+$", string=user_name_to_validate):
            raise ValueError("Username can only contain letters, numbers, underscores, and periods.")
        return user_name_to_validate

    @field_validator('mobile_number')
    def mobile_number_rules(cls, mobile_number_to_validate: str):
        try:
            # Parse the phone number with no region (automatically detects the region)
            phone_obj = phonenumbers.parse(mobile_number_to_validate, None)
            # Check if the phone number is a valid number
            if not phonenumbers.is_valid_number(phone_obj):
                raise ValueError("Invalid phone number format.")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError("Invalid phone number format.")

        return mobile_number_to_validate

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "jdoe@gmail.com",
                "mobile_number": "254740909890",
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
