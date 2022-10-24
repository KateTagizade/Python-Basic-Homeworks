from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ping")
def ping_pong():
    return {
        "message": "pong"
    }