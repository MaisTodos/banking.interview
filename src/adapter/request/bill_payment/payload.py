from pydantic import BaseModel


class BillPaymentPayload(BaseModel):
    amount: float
    payer_name: str