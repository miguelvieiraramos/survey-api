from presentation.errors.missing_param_error import MissingParamError
from presentation.protocols.http import HttpResponse, HttpRequest
from presentation.helpers.http_helpers import bad_request
from presentation.protocols.controller import Controller


class SignUpController(Controller):

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        required_fields = ['name', 'email', 'password', 'password_confirmation']
        for field in required_fields:
            if not http_request['body'].get(field):
                return bad_request(MissingParamError(field))
