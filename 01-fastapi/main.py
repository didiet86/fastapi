from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from /home/online/learn/fastapi/01-fastapi"}


@app.get("/hello1")
def hello1():
    return {"message": "Hello from /home/online/learn/fastapi/01-fastapi1"}
