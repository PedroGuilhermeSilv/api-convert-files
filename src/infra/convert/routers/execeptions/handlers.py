
from ninja import NinjaAPI

from src.core.convert.factory.creater.exceptions.erros import InvalidTypeForConvert

api = NinjaAPI()

# initializing handler

@api.exception_handler(InvalidTypeForConvert)
def service_unavailable(request, exc):
    return api.create_response(
        request,
        {"message": str(exc)},
        status=404,
    )