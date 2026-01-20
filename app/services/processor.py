from app.domain.transactions import Transaction
from app.schemas import PaymentDataRequest, PaymentDataResponse


class TransactionProcessor:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    def process(self, payload: PaymentDataRequest) -> PaymentDataResponse:
        return self.transaction.process(payload)
