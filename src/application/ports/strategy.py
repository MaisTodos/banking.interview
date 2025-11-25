from abc import ABC, abstractmethod

from src.adapter.request.payment import RequestPayment
from src.application.dto.response.payment_dto import PaymentDTO


class IPaymentStrategy(ABC):
    @abstractmethod
    def process(data: RequestPayment) -> PaymentDTO:
        pass
