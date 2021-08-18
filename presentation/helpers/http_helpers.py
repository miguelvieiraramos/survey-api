from presentation.errors.server_error import ServerError
from presentation.protocols.http import HttpResponse


def bad_request(error: Exception) -> HttpResponse:
    return HttpResponse(400, error)

def server_error() -> HttpResponse:
    return HttpResponse(500, ServerError())
