from src.adapter.request.pix.pix import PixRequest
from src.application.dto.response.payment_dto import PaymentDTO
from src.application.ports.pix import IPixPayment


class PixPayment(IPixPayment):
    @staticmethod
    def process(data: PixRequest):
        payload = data.payload
        print(f"[PIX] Enviando pagamento para chave {payload.pix_key}, valor {payload.amount}")
        return PaymentDTO(status="ok", provider="BankPix")
