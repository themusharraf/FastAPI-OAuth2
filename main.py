from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils import authenticate_user, get_password_hash, get_current_active_user, get_user, get_current_user, \
    ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY, create_access_token
from models import Token, db, User, UserInDB, TokenData
from datetime import timedelta

app = FastAPI()


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}



@app.get("/user/me", response_model=User)
async def read_user_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@app.get("/user/me/items")
async def read_own_items(current_users: User = Depends(get_current_active_user)):
    return [{"items_id": 1, "owner": current_users}]


