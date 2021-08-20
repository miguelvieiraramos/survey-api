from operator import itemgetter

from presentation.helpers.http_helpers import bad_request, server_error
from presentation.errors import InvalidParamError, MissingParamError
from presentation.protocols.email_validator import EmailValidator
from presentation.protocols.http import HttpResponse, HttpRequest
from presentation.protocols.controller import Controller


class SignUpController(Controller):

    def __init__(self, email_validator: EmailValidator):
        self.email_validator = email_validator

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            required_fields = ['name', 'email', 'password', 'password_confirmation']
            for field in required_fields:
                if not http_request['body'].get(field):
                    return bad_request(MissingParamError(field))
            password, password_confirmation, email = itemgetter('password', 'password_confirmation', 'email')(
                http_request['body'])
            if password != password_confirmation:
                return bad_request(InvalidParamError('confirmation_password'))
            is_valid: bool = self.email_validator.is_valid(email=email)
            if not is_valid:
                return bad_request(InvalidParamError('email'))
        except Exception:
            return server_error()
