from src.adapter.request.payment import RequestPayment
from src.application.decorators.application import application_exception
from src.application.dto.response.payment_dto import PaymentDTO
from src.application.use_case.strategy import PaymentStrategy


class ControllerPayment:
    @application_exception
    def handle_payment(data: RequestPayment) -> PaymentDTO:
        return PaymentStrategy.process(data)
