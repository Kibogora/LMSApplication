from typing import Optional,List
from fastapi import FastAPI,Path,Query
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses",
    version="0.1.1",
    terms_of_service="http://example.com/terms",
    contact={
        "name": "Kibogora",
        "url": "http://x-force.example.com/contact",
        "email":"kibogoran@gmail.com",
    },
    license_info={
        "name": "MIT",
        
    },
    
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None

@app.get("/user")
async def get_users():
    return users

@app.post("/user", response_model=List[User])
async def create_user(user: User):
    users.append(user)
    return "success"

@app.get("/user/{id}")
async def get_user(
    id: int = Path(..., description="The ID of the user you want to retrieve",gt=2),
    q: str = Query(None,max_length=5)           
):
    return  {"users": users[id], "query": q }