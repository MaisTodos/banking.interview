from src.adapter.request.ted.ted import TedRequest
from src.application.dto.response.payment_dto import PaymentDTO
from src.application.ports.ted import ITedPayment


class TedPayment(ITedPayment):
    @staticmethod
    def process(data: TedRequest):
        payload = data.payload
        print(f"[TED] Transferindo {payload.amount} para banco {payload.bank_code}-{payload.agency}/{payload.account_number}")
        return PaymentDTO(status="pending", provider="LegacyBank")
