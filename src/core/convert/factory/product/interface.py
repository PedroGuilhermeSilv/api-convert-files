from abc import ABC, abstractmethod

from pydantic import FilePath


class Converter(ABC):
    @abstractmethod
    def convert(self, path_file: FilePath) -> None:
        pass