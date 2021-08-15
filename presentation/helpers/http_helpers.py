from presentation.protocols.http import HttpResponse


def bad_request(error: Exception) -> HttpResponse:
    return HttpResponse(400, error)
