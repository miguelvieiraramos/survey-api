from presentation.errors.invalid_param_error import InvalidParamError
from presentation.errors.missing_param_error import MissingParamError
from presentation.protocols.email_validator import EmailValidator
from presentation.protocols.http import HttpResponse, HttpRequest
from presentation.helpers.http_helpers import bad_request
from presentation.protocols.controller import Controller


class SignUpController(Controller):

    def __init__(self, email_validator: EmailValidator):
        self.email_validator = email_validator

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        required_fields = ['name', 'email', 'password', 'password_confirmation']
        for field in required_fields:
            if not http_request['body'].get(field):
                return bad_request(MissingParamError(field))

        is_valid: bool = self.email_validator.is_valid(email=http_request['body'].get('email'))
        if not is_valid:
            return bad_request(InvalidParamError('email'))
