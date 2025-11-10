# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from app.camera import Camera

app = FastAPI()
camera = Camera()
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/video_feed")
def video_feed():
    return StreamingResponse(camera.generate_frames(),
                             media_type="multipart/x-mixed-replace; boundary=frame")
