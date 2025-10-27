from fastapi import FastAPI, Query
from decouple import config as env

app = FastAPI()

ENV_DATA = env('ENV_DATA')


@app.get("/ping")
async def ping():
    """Endpoint that returns pong ok message"""
    return {"pong": ENV_DATA}


@app.get("/uppercase")
async def uppercase(text: str = Query(..., description="Text to convert to uppercase")):
    """Endpoint that converts query parameter text to uppercase"""
    return {"uppercase": text.upper()}
