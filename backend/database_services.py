from typing import Dict

def get_user(username:str) -> Dict[str, str]:
    if username == "juan":
        return {"username":"juan", "password":"$2b$12$i/lJ1oS5aovi.hfl/og/Z.tZOhm7do2IxEQgoNqs7bXyWGLko5HeW"}
    return None