from operator import itemgetter

from domain.models.account import AccountModel
from domain.usecases.add_account import AddAccount
from presentation.helpers.http_helpers import bad_request, server_error, ok
from presentation.errors import InvalidParamError, MissingParamError
from presentation.protocols.email_validator import EmailValidator
from presentation.protocols.http import HttpResponse, HttpRequest
from presentation.protocols.controller import Controller


class SignUpController(Controller):

    def __init__(self, email_validator: EmailValidator, add_account: AddAccount):
        self.email_validator = email_validator
        self.add_account = add_account

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            required_fields = ['name', 'email', 'password', 'password_confirmation']
            for field in required_fields:
                if not http_request['body'].get(field):
                    return bad_request(MissingParamError(field))
            name, password, password_confirmation, email = itemgetter(
                'name', 'password', 'password_confirmation', 'email')(http_request['body'])
            if password != password_confirmation:
                return bad_request(InvalidParamError('confirmation_password'))
            is_valid: bool = self.email_validator.is_valid(email=email)
            if not is_valid:
                return bad_request(InvalidParamError('email'))
            account: AccountModel = self.add_account.add(name=name, email=email, password=password)
            return ok(vars(account))
        except Exception:
            return server_error()
