from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

#path parameter
@app.get("/user/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

#query parameter
@app.get("/items/")
async def read_items(name: Optional[str] = None, price: Optional[int] = None):
    return {"name": name, "price": price}

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

#POST body
@app.post("/users/")
async def create_user(user: dict):
    return {"created_user": user}