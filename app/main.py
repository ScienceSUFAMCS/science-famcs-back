from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from starlette import status
import uvicorn

app = FastAPI()


@app.get("/")
def root(request: Request):
    return RedirectResponse(request.url._url + "health")


@app.get("/health")
def health_endpoint():
    return JSONResponse(status_code=status.HTTP_200_OK, content={})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)