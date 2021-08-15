from presentation.errors.missing_param_error import MissingParamError
from presentation.helpers.http_helpers import bad_request
from presentation.protocols.http import HttpResponse, HttpRequest


class SignUpController:

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        if not http_request['body'].get('name'):
            return bad_request(MissingParamError('name'))

        if not http_request['body'].get('email'):
            return bad_request(MissingParamError('email'))
