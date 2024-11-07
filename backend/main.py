from fastapi import FastAPI, Depends, HTTPException, status, Header
from pydantic import BaseModel
from typing import Optional, Annotated
from jose import JWTError, jwt
from fastapi.middleware.cors import CORSMiddleware

from auth import validates_jwt, validates_login
from jwt_manage import encodeJWT
from database_services import add_user
from hash_password import get_password_hash

class LoginBody(BaseModel):
    username: str
    password: str

jwt_dependency = Annotated[dict, Depends(validates_jwt)]

# FastAPI app
app = FastAPI()

# Ruta de login
@app.post("/login")
async def login(login_request: LoginBody):
    user = validates_login(login_request.username, login_request.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = encodeJWT(login_request.username)
    return access_token

@app.post("/register")
async def register(login_request: LoginBody):
    result = add_user(username=login_request.username, password=get_password_hash(login_request.password))
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    return {"message": "User registered successfully"}

# Ruta protegida (requiere autenticación con Bearer token simple)
@app.get("/protected-route")
async def protected_route(jwt_data: jwt_dependency):
    if jwt_data:
        return jwt_data
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Not valid session"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080/", "http://127.0.0.1:8080/"],  # Especifica los orígenes de tu frontend
    allow_credentials=True,
    allow_methods=[""],  # Permite todos los métodos HTTP
    allow_headers=[""],  # Permite todos los encabezados necesarios
)