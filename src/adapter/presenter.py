from src.adapter.response import PaymentResponse


class PaymentPresenter:
    @staticmethod
    def success(data) -> PaymentResponse:
        return PaymentResponse(
            status=data.status, 
            provider=data.provider
        )
