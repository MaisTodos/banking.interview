from typing import Literal
from pydantic import BaseModel
from src.adapter.request.ted.payload import TedPayload

class TedRequest(BaseModel):
    transaction_type: Literal["ted"]
    payload: TedPayload
