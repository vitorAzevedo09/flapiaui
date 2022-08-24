from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import user

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
        )

@app.get("/")
async def root() -> dict[str, str]:
    return { "message": "vasco"}

app.include_router(user.router)
