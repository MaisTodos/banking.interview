from typing import Annotated, Union

from pydantic import Field
from src.adapter.request.bill_payment.bill_payment import BillPaymentRequest
from src.adapter.request.pix.pix import PixRequest
from src.adapter.request.ted.ted import TedRequest


RequestPayment = Annotated[Union[TedRequest, BillPaymentRequest, PixRequest], Field(discriminator='transaction_type')]
