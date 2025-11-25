from pydantic import BaseModel
from typing import Literal

from src.adapter.request.bill_payment.payload import BillPaymentPayload


class BillPaymentRequest(BaseModel):
    transaction_type: Literal["boleto"]
    payload: BillPaymentPayload
