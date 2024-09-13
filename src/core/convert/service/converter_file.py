
from src.core.convert.factory.creater.converter import ConverterFactory


class ConverterService():
    def __init__(self, converter: ConverterFactory):
        self.converter = converter

