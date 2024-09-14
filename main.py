from fastapi import FastAPI
import nest_asyncio
import uvicorn

app = FastAPI()
@app.get("/")
async def main():
    return {"Hello": "World"}

nest_asyncio.apply()
uvicorn.run(app, host="0.0.0.0")