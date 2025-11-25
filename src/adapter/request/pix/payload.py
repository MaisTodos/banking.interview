from typing import Optional
from pydantic import BaseModel


class PixPayload(BaseModel):
    amount: float
    pix_key: str
    description: Optional[str]
