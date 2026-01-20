from fastapi import FastAPI, HTTPException
from app.schemas import PaymentDataRequest, PaymentDataResponse
from app.services.factory import TransactionFactory
from app.services.processor import TransactionProcessor

app = FastAPI()


@app.post("/payment")
def handle_payment(data: PaymentDataRequest) -> PaymentDataResponse:
    try:
        transaction = TransactionFactory.get(data.transaction_type)
        processor = TransactionProcessor(transaction)
        return processor.process(data.payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
