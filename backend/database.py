# database.py
from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

# Cargar la URL desde las variables de entorno
DB_URL = config("DB_URL")
client = AsyncIOMotorClient(DB_URL)
database = client["tictacioDB"]
users_collection = database["usuarios"]
