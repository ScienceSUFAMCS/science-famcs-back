from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse
from starlette import status

health_router = APIRouter()


@health_router.get("/")
def root(request: Request):
    return RedirectResponse(request.url.url + "health")


@health_router.get("/health")
def health_endpoint():
    return JSONResponse(status_code=status.HTTP_200_OK, content={})
