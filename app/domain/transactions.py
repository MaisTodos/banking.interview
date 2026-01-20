from abc import ABC, abstractmethod

from app.schemas import (
    PaymentDataRequest,
    PaymentDataResponse,
    PixPayloadRequest,
    TedPayloadRequest,
    BoletoPayloadRequest,
)


class Transaction(ABC):
    @abstractmethod
    def process(self, data: PaymentDataRequest) -> PaymentDataResponse:
        pass


class PixProcessor(Transaction):
    def process(self, data: PaymentDataRequest) -> PaymentDataResponse:
        # --- integração simulada com provedor PIX ---
        data = PixPayloadRequest.model_validate(data)

        print(
            f"[PIX] Enviando pagamento para chave {data.pix_key}, "
            f"valor {data.amount}"
        )

        return PaymentDataResponse.model_validate(
            {"status": "ok", "provider": "BankPix"}
        )


class TedProcessor(Transaction):
    def process(self, data: PaymentDataRequest) -> PaymentDataResponse:
        # --- integração simulada com banco para TED ---
        data = TedPayloadRequest.model_validate(data)

        print(
            f"[TED] Transferindo {data.amount} para banco "
            f"{data.bank_code}-{data.agency}/{data.account_number}"
        )

        return PaymentDataResponse.model_validate(
            {"status": "pending", "provider": "LegacyBank"}
        )


class BoletoProcessor(Transaction):
    def process(self, data: PaymentDataRequest) -> PaymentDataResponse:
        # --- integração simulada com gateway de boletos ---
        data = BoletoPayloadRequest.model_validate(data)

        print(
            f"[BOLETO] Emitindo boleto no valor {data.amount} "
            f"para {data.payer_name}"
        )

        return PaymentDataResponse.model_validate(
            {"status": "issued", "provider": "BoletoGateway"}
        )
