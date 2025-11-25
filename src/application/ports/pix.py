from abc import ABC, abstractmethod

from src.adapter.request.pix.pix import PixRequest


class IPixPayment(ABC):
    @staticmethod
    @abstractmethod
    def process(data: PixRequest):
        pass
