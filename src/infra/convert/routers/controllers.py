import os

from django.http import FileResponse
from ninja import File, NinjaAPI, UploadedFile

from src.core.convert.factory.creater.converter_dynamic import (
    ManufacturingDynamicConverters,
)
from src.core.convert.factory.creater.exceptions.erros import InvalidTypeForConvert
from src.core.convert.service.converter_file import ConverterService
from src.core.convert.service.dto.input import InputConverter
from src.infra.convert.routers.dto.enum import TypeInput, TypeOutput
from src.infra.convert.routers.execeptions.handlers import service_unavailable

api = NinjaAPI()

@api.post("/convert/{typeInput}/to/{typeOutput}")
def convert(request, typeInput: TypeInput, typeOutput: TypeOutput, file: UploadedFile = File(...))->FileResponse:
    try:

        save_path = os.path.join("src/infra/convert/tmp/", file.name)
        with open(save_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        factory = ManufacturingDynamicConverters()
        service = ConverterService(factory)
        response = service.execute(InputConverter(typeInput=typeInput, typeOutput=typeOutput, pathFile=save_path))

        fileConverted = open(response.pathFile, 'rb')
    except InvalidTypeForConvert as e:
        return service_unavailable(request, e)


    return FileResponse(fileConverted, as_attachment=True, filename=response.fileName)

