from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import *

BATTERY_LEVEL = 98

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4000",
    "http://127.0.0.1:4000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/battery-level")
def batteryLevel():
    return {"battery": BATTERY_LEVEL}

