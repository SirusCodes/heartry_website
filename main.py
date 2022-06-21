import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

CWD = os.getcwd()

app.mount("/static", StaticFiles(directory=f"{CWD}/public/"), name="static")

templates = Jinja2Templates(directory=f"{CWD}/public/html/")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.get("/policy", response_class=HTMLResponse)
def policy(request: Request):
    return templates.TemplateResponse("policy.html",{"request": request})

@app.get("/install", response_class=HTMLResponse)
def install():
    return RedirectResponse("https://play.google.com/store/apps/details?id=com.darshan.heartry", status_code=302)