from abc import ABC, abstractmethod

from src.core.convert.factory.creater.dto.input import InputTypeConverter
from src.core.convert.factory.product.interface.abstract_converter import Converter


class ConverterFactory(ABC):
    @abstractmethod
    def create(self, input: InputTypeConverter) -> Converter:
        pass