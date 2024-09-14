import os

import pandas as pd
from pydantic import FilePath

from src.core.convert.factory.product.dto.output import OutputConvert
from src.core.convert.factory.product.interface.abstract_converter import Converter


class ConvertCsvToJson(Converter):
    def convert(self, path_file: FilePath) -> OutputConvert:
        try:
            name_file = os.path.splitext(os.path.basename(path_file))[0]
            csv_data_df = pd.read_csv(path_file, encoding='utf-8-sig' )             
        
            output_path = f"src/infra/convert/tmp/{name_file}.json"
            csv_data_df.to_json(orient='records', path_or_buf=output_path, force_ascii=False)
            return OutputConvert(fileName=name_file+".json", filePath=output_path)
        except Exception as e:
            raise e