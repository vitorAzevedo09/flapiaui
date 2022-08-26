
from fastapi import APIRouter, status, Depends

from typing import List
from pydantic import UUID4

from ..models.monthly_payment import MonthlyPayment
from ..schemas.monthly_payment import MonthlyPaymentOut, MonthlyPaymentCreate, MonthlyPaymentUpdate
from ..services.monthly_payment import MonthlyPaymentService, get_monthly_payment_service

router = APIRouter(prefix="/monthly_payments", tags=['MonthlyPayments'])


@router.post('/',
             status_code=status.HTTP_201_CREATED,
             response_model=MonthlyPaymentOut)
async def create_monthly_payment(user: MonthlyPaymentCreate,
                      monthly_payment_service: MonthlyPaymentService = Depends(get_monthly_payment_service)) -> MonthlyPayment:
    return monthly_payment_service.create(user)


@router.get('/',
            response_model=List[MonthlyPaymentOut])
async def list_monthly_payment(monthly_payment_service: MonthlyPaymentService = Depends(get_monthly_payment_service)) -> List[MonthlyPayment]:
    return monthly_payment_service.list()


@router.get('/{id}',
            response_model=MonthlyPaymentOut)
async def get_monthly_payment(id: UUID4,
                   monthly_payment_service: MonthlyPaymentService = Depends(get_monthly_payment_service)) -> MonthlyPayment:
    return monthly_payment_service.get(id=id)


@router.patch('/{id}',
              response_model=MonthlyPaymentOut)
async def update_monthly_payment(id: UUID4,
                      user: MonthlyPaymentUpdate,
                      monthly_payment_service: MonthlyPaymentService = Depends(get_monthly_payment_service)) -> MonthlyPayment:
    return monthly_payment_service.update(id=id, obj=user)


@router.delete('/{id}',
               status_code=status.HTTP_200_OK)
async def delete_monthly_payment(
        id: UUID4,
        monthly_payment_service: MonthlyPaymentService = Depends(get_monthly_payment_service)) -> None:
    return monthly_payment_service.delete(id=id)
