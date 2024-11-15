from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
async def index():
    return {"name": "Hi there"}