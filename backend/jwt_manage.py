from jose import JWTError, jwt
from typing import Dict

JWT_SECRET = "secret"
JWT_ALGORITHM = "algoritmo"

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token
    except:
        return {}
    
def encodeJWT(id_user: str) -> Dict[str, str]:
    payload = {"userID": id_user}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"token": token}