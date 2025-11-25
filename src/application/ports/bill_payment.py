from abc import ABC, abstractmethod

from src.adapter.request.bill_payment.bill_payment import BillPaymentRequest


class IBillPayment(ABC):
    @staticmethod
    @abstractmethod
    def process(data: BillPaymentRequest):
        pass
