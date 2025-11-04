from fastapi import FastAPI
from pydantic import BaseModel
from processor import TransactionProcessor

app = FastAPI()

class PaymentData(BaseModel):
    transaction_type: str
    payload: dict

@app.post("/payment")
def handle_payment(data: PaymentData):
    return TransactionProcessor(data.transaction_type, data.payload).process()
