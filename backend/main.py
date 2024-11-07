from fastapi import FastAPI, Depends, HTTPException, status, Header
from pydantic import BaseModel
from typing import Optional, Annotated
from jose import JWTError, jwt
from fastapi.middleware.cors import CORSMiddleware

from auth import validates_jwt, validates_login
from jwt_manage import encodeJWT

class LoginRequest(BaseModel):
    username: str
    password: str

jwt_dependency = Annotated[dict, Depends(validates_jwt)]

# FastAPI app
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5000/", "http://127.0.0.1:5173/"],  # Añade la URL de tu frontend aquí
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

# Ruta de login
@app.post("/login")
async def login(login_request: LoginRequest):
    user = validates_login(login_request.username, login_request.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = encodeJWT(login_request.username)
    return access_token

# Ruta protegida (requiere autenticación con Bearer token simple)
@app.get("/protected-route")
async def protected_route(jwt_data: jwt_dependency):
    if jwt_data:
        return jwt_data
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Not valid session"
    )
