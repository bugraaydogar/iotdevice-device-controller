from fastapi import FastAPI, APIRouter


BATTERY_LEVEL = 55
SPEED_LEVEL = 90
ANGULAR_FREEDOM = 245
VERSION_V1 = 1.0

app = FastAPI()

version_v1 = APIRouter()

# Common API
@app.get("/version")
async def get_api_version():
    return {"version": VERSION_V1}

# Features API
@version_v1.get("/features")
async def get_features_list():
    return {"features": ["speed", "batterylevel", "angularfreedom"]}


# Battery API
@version_v1.get("/batterylevel")
async def get_battery_level_v1():
    return {"level": BATTERY_LEVEL}

# Speed API
@version_v1.get("/speed")
async def get_speed_level_v1():
    return {"speed": SPEED_LEVEL}

# Robotic API
@version_v1.get("/angularfreedom")
async def get_angularfreedom_v1():
    return {"angle": ANGULAR_FREEDOM}


app.include_router(version_v1, prefix='/v1')
