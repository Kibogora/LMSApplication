from typing import Optional, List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None

# Corrected the route by adding a leading "/"
@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "success"

@router.get("/user/{id}")
async def get_user(id: int):
    try:
        return {"user": users[id]}
    except IndexError:
        return {"error": "User not found"}