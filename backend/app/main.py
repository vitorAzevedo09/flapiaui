from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.app.routers import default
from .api.core.config import settings

app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)

origins = ['*']

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        )

app.include_router(default.router)
