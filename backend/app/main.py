from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import user
from .routers import payment_book
from .routers import monthly_payment
from .routers import oauth2

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
app.include_router(payment_book.router)
app.include_router(monthly_payment.router)
app.include_router(oauth2.router)
