from typing import Literal
from pydantic import BaseModel

from src.adapter.request.pix.payload import PixPayload

class PixRequest(BaseModel):
    transaction_type: Literal["pix"]
    payload: PixPayload
