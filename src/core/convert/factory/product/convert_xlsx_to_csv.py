import boto3
from django.conf import settings

from src.core.convert.factory.product.dto.output import OutputConvert
from src.core.convert.factory.product.interface.abstract_converter import Converter

PATH_S3 = "https://s3.tebi.io/convert-files/"


class ConvertXlsxToCsv(Converter):
    def convert(self, file) -> OutputConvert:
        try:
            s3 = boto3.resource(
                service_name="s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                endpoint_url=settings.ENDPOINT_URL,
            )

            output_name_file = f"{file.name}.csv".replace(".xlsx", "")

            s3.Bucket("convert-files").put_object(
                Key=output_name_file, Body=file.file, ACL="public-read"
            )

            return OutputConvert(
                fileName=file.name + ".csv", filePath=PATH_S3 + output_name_file
            )

        except Exception as e:
            raise e
