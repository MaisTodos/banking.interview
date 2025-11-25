from src.adapter.request.payment import RequestPayment
from src.application.dto.response.payment_dto import PaymentDTO
from src.application.use_case.bill_payment import BillPayment
from src.application.use_case.pix import PixPayment
from src.application.use_case.ted import TedPayment


class PaymentStrategy:
    @staticmethod
    def process(data: RequestPayment) -> PaymentDTO:
        if data.transaction_type == "pix":
            return PixPayment.process(data)
        elif data.transaction_type == "ted":
            return TedPayment.process(data)
        elif data.transaction_type == "boleto":
            return BillPayment.process(data)
        else:
            raise ValueError("Unsupported transaction type")

