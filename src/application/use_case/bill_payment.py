from src.adapter.request.bill_payment.bill_payment import BillPaymentRequest
from src.application.dto.response.payment_dto import PaymentDTO
from src.application.ports.bill_payment import IBillPayment


class BillPayment(IBillPayment):
    @staticmethod
    def process(data: BillPaymentRequest):
        payload = data.payload
        print(f"[BOLETO] Emitindo boleto no valor {payload.amount} para {payload.payer_name}")
        return PaymentDTO(status="issued", provider="BoletoGateway")
