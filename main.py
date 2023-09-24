from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()


@app.get("/")
async def root(request: Request):
    return RedirectResponse(request.url._url + "health")


@app.get("/health")
async def health_endpoint():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)