import os

from django.http import FileResponse
from ninja import File, NinjaAPI, UploadedFile

from src.core.convert.factory.creater.converter import ConverterFactory
from src.core.convert.service.converter_file import ConverterService
from src.core.convert.service.dto.input import InputConverter

api = NinjaAPI()

@api.post("/convert/{typeInput}/to/{typeOutput}")
def convert(request, typeInput: str, typeOutput: str, file: UploadedFile = File(...))->FileResponse:
    old_files = os.listdir("src/infra/convert/tmp/")
    for old_file in old_files:
        os.remove(os.path.join("src/infra/convert/tmp/", old_file))
    save_path = os.path.join("src/infra/convert/tmp/", file.name)
    with open(save_path, 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)

    factory = ConverterFactory()
    service = ConverterService(factory)
    response = service.converter.convert_file(InputConverter(typeInput=typeInput, typeOutput=typeOutput, pathFile=save_path))

    if not os.path.exists(response.pathFile):
        return {"error": "Converted file not found"}
    fileCsv = open(response.pathFile, 'rb')

    return FileResponse(fileCsv, as_attachment=True, filename=response.fileName)

