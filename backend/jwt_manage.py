from jose import JWTError, jwt
from typing import Dict

JWT_SECRET = "secret"
JWT_ALGORITHM = "HS256"

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decoded_token
    except:
        return None
    
def encodeJWT(username: str) -> Dict[str, str]:
    payload = {"username": username}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"token": token}