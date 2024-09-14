


import os

from src.core.convert.factory.creater.dto.input import InputTypeConverter
from src.core.convert.factory.creater.interface.abstract_factory import ConverterFactory
from src.core.convert.service.dto.input import InputConverter
from src.core.convert.service.dto.output import OutputConverter


class ConverterService():
    def __init__(self, factory_converter: ConverterFactory):
        self.factory_converter = factory_converter

    def execute(self, input: InputConverter)-> OutputConverter:
        try:
            converter = self.factory_converter.create(InputTypeConverter(typeInput=input.typeInput,typeOutput=input.typeOutput))
            response = converter.convert(path_file=input.pathFile)
            return OutputConverter(fileName=response.fileName, pathFile=response.filePath)

        except Exception as e:
            raise e

    