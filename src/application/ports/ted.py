from abc import ABC, abstractmethod
from src.adapter.request.ted.ted import TedRequest


class ITedPayment(ABC):
    @staticmethod
    @abstractmethod
    def process(data: TedRequest):
        pass
