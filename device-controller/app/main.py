from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import *

MAX_SPEED = 98

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
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
    return {"speed": randint(0, 100), "maxSpeed": MAX_SPEED}
