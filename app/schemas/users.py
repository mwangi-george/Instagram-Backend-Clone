from pydantic import BaseModel, EmailStr, Field


class ActionConfirm(BaseModel):
    msg: str


class UserCreate(BaseModel):
    """ Validation Schema for creating a user """
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(..., min_length=3, max_length=100)
    password: str = Field(..., min_length=8, max_length=255)

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "jdoe@gmail.com",
                "password": "zxcv",
            }
        }


class TokenCreate(BaseModel):
    access_token: str
    token_type: str


