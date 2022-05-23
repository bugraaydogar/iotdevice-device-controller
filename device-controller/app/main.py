from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from .snapd import SnapdClient

app = FastAPI()
snap_client = SnapdClient()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def pong():
    return {"ping": "pong!"}


@app.get("/battery-level")
def batteryLevel():
    return {"battery": 50}


@app.get("/system-info")
def system_info():
    return snap_client.snap_system_info()


@app.post("/refresh")
def refresh():
    response = snap_client.refresh()
    return response


@app.post("/revert")
def revert(snaps: List[str]):
    response = snap_client.revert(snaps)
    return response

