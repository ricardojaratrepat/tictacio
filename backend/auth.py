from auth.decodeAuth import decodeJWT
from fastapi import HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True, level: int = 0):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.level = level

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
    
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Invalid authentication scheme.",
                )
            return self.verify_jwt(credentials.credentials)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authorization code.",
            )

    def verify_jwt(self, jwtoken: str) -> models.Dispatcher:
        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None

        if payload:
            pass
        else:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="d: Invalid token or expired token.",
            )