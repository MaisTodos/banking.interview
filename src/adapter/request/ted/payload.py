from pydantic import BaseModel


class TedPayload(BaseModel):
    bank_code: str
    agency: str
    account_number: str
    amount: float
