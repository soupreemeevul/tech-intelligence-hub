from fastapi import FastAPI

app = FastAPI(title="Tech Intelligence Hub")


@app.get("/")
def home():
    return {
        "message": "Tech Intelligence Hub is online!"
    }