from pydantic import BaseModel

db = {
    "mrx": {
        "username": "mrx",
        "full_name": "The Musharraf",
        "email": "mrxtest@gmail.com",
        "hashed_password": "$2b$12$V2eOx9FOFEV1U9zPm0ixguXsn/1Ep9BErq81wCVpsgGI7fcEu9SYi",
        "disabled": False
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str or None = None


class User(BaseModel):
    username: str
    email: str or None = None
    full_name: str or None = None
    disabled: bool or None = None


class UserInDB(User):
    hashed_password: str
