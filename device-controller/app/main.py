from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import *

MAX_SPEED = 90

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

@app.get("/speed-level")
def batteryLevel():
    return {"speed": randint(0, MAX_SPEED+15), "maxSpeed": MAX_SPEED}

