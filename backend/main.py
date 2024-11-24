from fastapi import FastAPI, Depends, HTTPException, status, Header
from typing import Optional, Annotated
from jose import JWTError, jwt
from fastapi.middleware.cors import CORSMiddleware

from auth import validates_jwt, validates_login
from jwt_manage import encodeJWT
from database_services import add_user

from models import User

from database import client
import logging

jwt_dependency = Annotated[dict, Depends(validates_jwt)]


app = FastAPI()


# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_db_client():
    try:
        # Probar la conexión ejecutando una operación simple
        await client.admin.command('ping')
        logger.info("Successfully connected to MongoDB")
    except Exception as e:
        logger.error("Failed to connect to MongoDB", exc_info=True)
        raise e  # Detiene el inicio del servidor si falla la conexión

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
    logger.info("Disconnected from MongoDB")

# Ruta de login
@app.post("/login")
async def login(login_request: User):
    user = await validates_login(login_request.username, login_request.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = encodeJWT(login_request.username)
    return access_token

@app.post("/register")
async def register(login_request: User):
    result = await add_user(username=login_request.username, password=login_request.password)
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
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080"],  # Especifica los orígenes de tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados necesarios
)