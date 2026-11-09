from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Tech Intelligence Hub")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/dashboard")
def dashboard():
    return FileResponse("static/index.html")

@app.get("/")
def home():
    return {
        "message": "Tech Intelligence Hub is online!"
    }

@app.get("/articles")
def get_articles():
    return [
        {
            "id": 1,
            "title": "Exploring AI Agent Frameworks",
            "category": "AI Agents",
            "source": "Sample Article"
        },
        {
            "id": 2,
            "title": "Building Reliable DevOps Automation",
            "category": "DevOps",
            "source": "Sample Article"
        }
    ]