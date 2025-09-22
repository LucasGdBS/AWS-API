from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/ping")
async def ping():
    """Endpoint that returns pong ok message"""
    return {"pong": "ok"}


@app.get("/uppercase")
async def uppercase(text: str = Query(..., description="Text to convert to uppercase")):
    """Endpoint that converts query parameter text to uppercase"""
    return {"uppercase": text.upper()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)