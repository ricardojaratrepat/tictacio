from fastapi import Security, HTTPException, Depends
from fastapi.security import HTTPBearer
from jwt_manage import decodeJWT
from hash_password import verify_password
from database_services import get_user


JWT_header = HTTPBearer()


async def validates_jwt(
    jwt_header = Security(JWT_header),
):

    decode = decodeJWT(jwt_header.credentials)

    if not decode:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    user_data = await get_user(decode["username"])

    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    return user_data


async def validates_login(username:str, password:str):

    user_data = await get_user(username)

    if bool(user_data) and verify_password(plain_password=password, hashed_password=user_data["password"]):
        return True
    return False
    