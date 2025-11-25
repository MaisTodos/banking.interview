from fastapi import FastAPI

from src.adapter.request.payment import RequestPayment
from src.adapter.controller import ControllerPayment
from src.adapter.response import PaymentResponse

app = FastAPI()


@app.post("/payment")
def payment(request: RequestPayment) -> PaymentResponse:
    return ControllerPayment.handle_payment(request)
