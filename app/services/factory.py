from app.enums import TransactionTypeEnum
from app.domain.transactions import (
    Transaction,
    BoletoProcessor,
    PixProcessor,
    TedProcessor,
)


class TransactionFactory:
    _registry = {
        TransactionTypeEnum.PIX: PixProcessor(),
        TransactionTypeEnum.TED: TedProcessor(),
        TransactionTypeEnum.BOLETO: BoletoProcessor(),
    }

    @classmethod
    def get(cls, transaction_type: TransactionTypeEnum) -> Transaction:
        try:
            return cls._registry[transaction_type]
        except KeyError:
            raise ValueError(
                f"Unsupported transaction type: {transaction_type}"
            )
