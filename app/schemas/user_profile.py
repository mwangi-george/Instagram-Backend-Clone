from pydantic import BaseModel


class UserProfileSchema(BaseModel):
    username: str
    email: str
    name: str | None = None
    bio: str | None = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "jdoe",
                "email": "johndoe@gmail.com",
                "name": "John Doe",
                "bio": "Software Engineer"
            }
        }
