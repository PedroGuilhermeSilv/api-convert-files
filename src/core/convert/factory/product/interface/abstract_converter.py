from abc import ABC, abstractmethod

from src.core.convert.factory.product.dto.output import OutputConvert


class Converter(ABC):
    @abstractmethod
    def convert(self, file) -> OutputConvert:
        pass
