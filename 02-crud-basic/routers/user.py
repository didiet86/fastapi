from fastapi import APIRouter, HTTPException
from schemas.user import User

router = APIRouter()

# In-memory database
users: list[User] = []

@router.post("/users/")
def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully", "user": user}

@router.get("/users/")
def get_users():
    return users

@router.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for user in enumerate(users):
        if user.id == user_id:
            users[user] = updated_user
            return {"message": "User updated successfully", "user": updated_user}
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in enumerate(users):
        if user.id == user_id:
            users.pop(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")