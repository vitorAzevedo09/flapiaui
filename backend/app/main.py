from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import api 
from app.core import settings

app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)

origins = ['*']

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        )

app.include_router(api.router)
