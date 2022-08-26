
from fastapi import APIRouter, status, Depends

from typing import List
from pydantic import UUID4

from ..models.payment_book import PaymentBook
from ..schemas.payment_book import PaymentBookOut, PaymentBookCreate, PaymentBookUpdate
from ..services.payment_book import PaymentBookService, get_payment_book_service

from ..dependencies import is_admin

router = APIRouter(
        prefix="/payment_books",
        tags=['PaymentBooks'],
        dependencies=[
            Depends(is_admin)
            ])


@router.post('/',
             status_code=status.HTTP_201_CREATED,
             response_model=PaymentBookOut)
async def create_payment_book(payment_book: PaymentBookCreate,
                      payment_book_service: PaymentBookService = Depends(get_payment_book_service)) -> PaymentBook:
    return payment_book_service.create(payment_book)


@router.get('/',
            response_model=List[PaymentBookOut])
async def list_payment_book(payment_book_service: PaymentBookService = Depends(get_payment_book_service)) -> List[PaymentBook]:
    return payment_book_service.list()


@router.get('/{id}',
            response_model=PaymentBookOut)
async def get_payment_book(id: UUID4,
                   payment_book_service: PaymentBookService = Depends(get_payment_book_service)) -> PaymentBook:
    return payment_book_service.get(id=id)


@router.patch('/{id}',
              response_model=PaymentBookOut)
async def update_payment_book(id: UUID4,
                      payment_book: PaymentBookUpdate,
                      payment_book_service: PaymentBookService = Depends(get_payment_book_service)) -> PaymentBook:
    return payment_book_service.update(id=id, obj=payment_book)


@router.delete('/{id}',
               status_code=status.HTTP_200_OK)
async def delete_payment_book(
        id: UUID4,
        payment_book_service: PaymentBookService = Depends(get_payment_book_service)) -> None:
    return payment_book_service.delete(id=id)
