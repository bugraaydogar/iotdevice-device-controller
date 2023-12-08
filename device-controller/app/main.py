from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

BATTERY_LEVEL = 90
BATTERY_LEVEL_MAX = 100
SPEED_LEVEL = 90
SPEED_LEVEL_MAX = 100
ANGULAR_FREEDOM = 245
ANGULAR_FREEDOM_ROTATION = "left"
VERSION = 1.0

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

version_v1 = APIRouter()
version_v2 = APIRouter()

# Common API
@app.get("/version")
async def get_api_version():
    return {"version": VERSION}

# Features API
@version_v1.get("/features")
async def get_features_list_v1():
    return {"features": ["speed", "batterylevel", "angularfreedom"]}


@version_v2.get("/features")
async def get_features_list_v2():
    return {"features": ["speed", "batterylevel", "angularfreedom"]}


# Battery API
@version_v1.get("/batterylevel")
async def get_battery_level_v1():
    return {"level": BATTERY_LEVEL}

@version_v2.get("/batterylevel")
async def get_battery_level_v2():
    return {"level": BATTERY_LEVEL, "max_capacity": BATTERY_LEVEL_MAX}


# Speed API
@version_v1.get("/speed")
async def get_speed_level_v1():
    return {"speed": SPEED_LEVEL}

@version_v2.get("/speed")
async def get_speed_level_v2():
    return {"speed": SPEED_LEVEL, "max_speed": SPEED_LEVEL_MAX}

# Robotic API
@version_v1.get("/angularfreedom")
async def get_angularfreedom_v1():
    return {"angle": ANGULAR_FREEDOM}

@version_v2.get("/angularfreedom")
async def get_angularfreedom_v2():
    return {"angle": ANGULAR_FREEDOM, "rotation": ANGULAR_FREEDOM_ROTATION}


app.include_router(version_v1, prefix='/v1')
app.include_router(version_v2, prefix='/v2')