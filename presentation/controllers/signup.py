from presentation.errors.missing_param_error import MissingParamError
from presentation.protocols.http import HttpResponse, HttpRequest


class SignUpController:

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        if not http_request['body'].get('name'):
            return HttpResponse(400, MissingParamError('name'))

        if not http_request['body'].get('email'):
            return HttpResponse(400, MissingParamError('email'))
