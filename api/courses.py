from typing import Optional,List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None

@router.get("/courses")
async def read_courses():
    return {"courses": []}

@router.post("/courses")
async def create_course_api():
    return {"courses": []}

@router.get("/user/{id}")
async def read_course():
    return {"courses":[]}

@router.patch("/courses/{id}")
async def update_course():
    return {"courses": []}

@router.delete("/courses/{id}")
async def delete_course():
    return {"courses": []}

@router.get("/courses/:id/sections")    
async def read_course_sections():
    return {"courses": []}
      
