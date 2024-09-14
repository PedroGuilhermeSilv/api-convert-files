from abc import ABC, abstractmethod

from pydantic import FilePath

from src.core.convert.factory.product.dto.output import OutputConvert


class Converter(ABC):
    @abstractmethod
    def convert(self, path_file: FilePath) -> OutputConvert:
        pass