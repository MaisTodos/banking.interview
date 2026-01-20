from enum import Enum


class TransactionTypeEnum(Enum):
    PIX = "pix"
    TED = "ted"
    BOLETO = "boleto"
