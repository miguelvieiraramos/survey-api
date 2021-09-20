from operator import itemgetter

from src.domain.models.account import AccountModel
from src.domain.usecases.add_account import AddAccount, AddAccountModel
from src.presentation.helpers.http_helpers import bad_request, server_error, ok
from src.presentation.errors import InvalidParamError, MissingParamError
from src.presentation.protocols.email_validator import EmailValidator
from src.presentation.protocols.http import HttpResponse, HttpRequest
from src.presentation.protocols.controller import Controller


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
            account: AccountModel = self.add_account.add(AddAccountModel(name, email, password))
            return ok(vars(account))

        except Exception:
            return server_error()
