from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Ai Trade API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve index.html at root
@app.get("/")
def read_root():
    if os.path.exists("index.html1"):  # Check for index.html or index.html1
        return FileResponse("index.html1")
    elif os.path.exists("index.html"):
        return FileResponse("index.html")
    return {"status": "online", "message": "index.html not found"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
