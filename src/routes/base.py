from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter(
     prefix="/api/v1",tags=["Api_v1"]
)

@base_router.get("/")
async def welcome():   
    APP_NAME=os.getenv("APP_NAME")
    return {
        "app_name": APP_NAME,
        "app_version": "shko",
    }
