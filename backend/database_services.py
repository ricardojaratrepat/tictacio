from typing import Optional, Dict
from models import User
from database import users_collection  # Asegúrate de que esté importado correctamente
from bson import ObjectId
from fastapi import HTTPException
from pydantic import BaseModel

from hash_password import get_password_hash

# Servicio para obtener un usuario por su nombre de usuario
async def get_user(username: str) -> Optional[Dict[str, str]]:
    user = await users_collection.find_one({"username": username})
    if user:
        return {"username": user["username"], "password": user["password"]}
    return None

# Servicio para agregar un nuevo usuario
async def add_user(username: str, password: str) -> Dict[str, str]:
    # Verificar si el usuario ya existe
    existing_user = await get_user(username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hashear la contraseña antes de guardarla
    hashed_password = get_password_hash(password)
    user_data = {"username": username, "password": hashed_password}
    await users_collection.insert_one(user_data)
    
    # Retornar el usuario creado (sin mostrar la contraseña hasheada)
    return {"username": username}