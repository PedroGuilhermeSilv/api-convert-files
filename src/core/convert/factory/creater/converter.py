

from src.core.convert.factory.product.convert_xlsx_to_csv import ConvertXlsxToCsv
from src.core.convert.service.dto.input import InputConverter
from src.core.convert.service.dto.output import OutputConverter


class ConverterFactory:
    def convert_file(self, input: InputConverter)-> OutputConverter:
        if input.typeInput == "xlsx" and input.typeOutput == "csv":
            converter = ConvertXlsxToCsv()
            path = converter.convert(input.pathFile)
            return path