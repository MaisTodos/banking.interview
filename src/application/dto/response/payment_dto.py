from dataclasses import dataclass


@dataclass(init=True)
class PaymentDTO:
    status: str
    provider: str
