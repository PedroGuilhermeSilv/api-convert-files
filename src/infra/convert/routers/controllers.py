from ninja import File, NinjaAPI, UploadedFile

from src.core.convert.factory.creater.converter_dynamic import (
    ManufacturingDynamicConverters,
)
from src.core.convert.factory.creater.exceptions.erros import InvalidTypeForConvert
from src.core.convert.service.converter_file import ConverterService
from src.core.convert.service.dto.input import InputConverter
from src.infra.convert.routers.dto.enum import TypeInput, TypeOutput
from src.infra.convert.routers.dto.output import OutputControllerConvert
from src.infra.convert.routers.execeptions.handlers import service_unavailable
from django.http import FileResponse
api = NinjaAPI()


@api.post("/convert/{typeInput}/to/{typeOutput}")
def convert(
    request,
    typeInput: TypeInput,
    typeOutput: TypeOutput,
    file: UploadedFile = File(...),
) -> FileResponse:
    try:
        manager_factory = ManufacturingDynamicConverters()
        service = ConverterService(manager_factory)
        response = service.execute(
            InputConverter(
                typeInput=typeInput,
                typeOutput=typeOutput,
                file=file,
            )
        )

    except InvalidTypeForConvert as e:
        return service_unavailable(request, e)
    except Exception as e:
        raise e

    return FileResponse(filename=response.fileName, as_attachment=True)
