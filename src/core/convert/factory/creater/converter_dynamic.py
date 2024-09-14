

from src.core.convert.factory.creater.dto.input import InputTypeConverter
from src.core.convert.factory.creater.exceptions.erros import InvalidTypeForConvert
from src.core.convert.factory.creater.interface.abstract_factory import ConverterFactory
from src.core.convert.factory.product.convert_csv_to_json import ConvertCsvToJson
from src.core.convert.factory.product.convert_json_to_csv import ConvertJsonToCsv
from src.core.convert.factory.product.convert_xlsx_to_csv import ConvertXlsxToCsv
from src.core.convert.factory.product.interface.abstract_converter import Converter


class ManufacturingDynamicConverters(ConverterFactory):
    def create(self, input: InputTypeConverter)-> Converter:
        if input.typeInput == "xlsx" and input.typeOutput == "csv":
            return  ConvertXlsxToCsv()
        if input.typeInput == "csv" and input.typeOutput == "json":
            return  ConvertCsvToJson()
        if input.typeInput == "json" and input.typeOutput == "csv":
            return  ConvertJsonToCsv()
        else:
            raise InvalidTypeForConvert
        

