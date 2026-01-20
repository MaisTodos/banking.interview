from pydantic import BaseModel, Field
from decimal import Decimal
from app.enums import TransactionTypeEnum


class PaymentDataRequest(BaseModel):
    transaction_type: TransactionTypeEnum
    payload: dict


class PaymentDataResponse(BaseModel):
    status: str
    provider: str


class BaseRequest(BaseModel):
    amount: Decimal = Field(..., decimal_places=2)


class PixPayloadRequest(BaseRequest):
    pix_key: str
    description: str | None = None


class TedPayloadRequest(BaseRequest):
    bank_code: str
    agency: str
    account_number: str


class BoletoPayloadRequest(BaseRequest):
    payer_name: str
