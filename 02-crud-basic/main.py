from fastapi import FastAPI
from routers import user

app = FastAPI()

# Include router
app.include_router(user.router)
