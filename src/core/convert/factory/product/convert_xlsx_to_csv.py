import os

import pandas as pd
from pydantic import FilePath

from src.core.convert.factory.product.interface import Converter
from src.core.convert.service.dto.output import OutputConverter


class ConvertXlsxToCsv(Converter):
    def convert(self, path_file: FilePath) -> OutputConverter:
        try:
            name_file = os.path.splitext(os.path.basename(path_file))[0]
            excel_data_df = pd.read_excel(path_file)            
        
            output_path = f"src/infra/convert/tmp/{name_file}.csv"
            excel_data_df.to_csv(output_path, index=False, encoding='utf-8')
            return OutputConverter(fileName=name_file+".csv", pathFile=output_path)
        except Exception as e:
            print(f"Error: {e}")
            raise e