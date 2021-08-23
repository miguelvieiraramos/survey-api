from operator import itemgetter
from unittest.mock import MagicMock

from domain.models.account import AccountModel
from domain.usecases.add_account import AddAccount
from presentation.controllers.signup import SignUpController
from presentation.errors import InvalidParamError, MissingParamError, ServerError
from presentation.protocols.email_validator import EmailValidator


class EmailValidatorStub(EmailValidator):
    def is_valid(self, email: str) -> bool:
        return True


class AddAccountStub(AddAccount):
    def add(self, name: str, email: str, password: str) -> AccountModel:
        return AccountModel(
            id='valid_id',
            name='valid_name',
            email='valid_email@mail.com',
            password='valid_password'
        )


def make_add_account() -> AddAccount:
    return AddAccountStub()


def make_email_validator():
    return EmailValidatorStub()


def make_sut():
    email_validator_stub = make_email_validator()
    add_account_stub = make_add_account()
    return {
        'sut': SignUpController(email_validator=email_validator_stub, add_account=add_account_stub),
        'email_validator_stub': email_validator_stub,
        'add_account_stub': add_account_stub
    }


def test_should_return_400_if_no_name_is_provided():
    sut = itemgetter('sut')(make_sut())
    http_request = {
        'body': {
            'email': 'any_email@mail.com',
            'password': 'any_password',
            'password_confirmation': 'any_password',
        }
    }
    http_response = sut.handle(http_request)
    assert http_response.status_code == 400
    assert isinstance(http_response.body, MissingParamError)
    assert http_response.body.args[0] == 'Missing param: name'


def test_should_return_400_if_no_email_is_provided():
    sut = itemgetter('sut')(make_sut())
    http_request = {
        'body': {
            'name': 'any_name',
            'password': 'any_password',
            'password_confirmation': 'any_password',
        }
    }
    http_response = sut.handle(http_request)
    assert http_response.status_code == 400
    assert isinstance(http_response.body, MissingParamError)
    assert http_response.body.args[0] == 'Missing param: email'


def test_should_return_400_if_no_password_is_provided():
    sut = itemgetter('sut')(make_sut())
    http_request = {
        'body': {
            'name': 'any_name',
            'email': 'any_email@mail.com',
            'password_confirmation': 'any_password',
        }
    }
    http_response = sut.handle(http_request)
    assert http_response.status_code == 400
    assert isinstance(http_response.body, MissingParamError)
    assert http_response.body.args[0] == 'Missing param: password'


def test_should_return_400_if_no_password_confirmation_is_provided():
    sut = itemgetter('sut')(make_sut())
    http_request = {
        'body': {
            'name': 'any_name',
            'email': 'any_email@mail.com',
            'password': 'any_password',
        }
    }
    http_response = sut.handle(http_request)
    assert http_response.status_code == 400
    assert isinstance(http_response.body, MissingParamError)
    assert http_response.body.args[0] == 'Missing param: password_confirmation'


def test_should_return_400_if_invalid_email_is_provided():
    sut, email_validator_stub = itemgetter('sut', 'email_validator_stub')(make_sut())
    email_validator_stub.is_valid = MagicMock(return_value=False)
    http_request = {
        'body': {
            'name': 'any_name',
            'email': 'any_email@mail.com',
            'password': 'any_password',
            'password_confirmation': 'any_password',
        }
    }
    http_response = sut.handle(http_request)
    assert http_response.status_code == 400
    assert isinstance(http_response.body, InvalidParamError)
    assert http_response.body.args[0] == 'Invalid param: email'


def test_should_return_400_if_invalid_password_confirmation_is_provided():
    sut = itemgetter('sut')(make_sut())
    http_request = {
        'body': {
            'name': 'any_name',
            'email': 'any_email@mail.com',
            'password': 'any_password',
            'password_confirmation': 'invalid_password',
        }
    }
    http_response = sut.handle(http_request)
    assert http_response.status_code == 400
    assert isinstance(http_response.body, InvalidParamError)
    assert http_response.body.args[0] == 'Invalid param: confirmation_password'


def test_should_call_EmailValidator_with_correct_email():
    sut, email_validator_stub = itemgetter('sut', 'email_validator_stub')(make_sut())
    email_validator_stub.is_valid = MagicMock()
    http_request = {
        'body': {
            'name': 'any_name',
            'email': 'any_email@mail.com',
            'password': 'any_password',
            'password_confirmation': 'any_password',
        }
    }
    sut.handle(http_request)
    email_validator_stub.is_valid.assert_called_with(email='any_email@mail.com')


def test_should_call_AddAccount_with_correct_params():
    sut, add_account_stub = itemgetter('sut', 'add_account_stub')(make_sut())
    add_account_stub.add = MagicMock()
    http_request = {
        'body': {
            'name': 'any_name',
            'email': 'any_email@mail.com',
            'password': 'any_password',
            'password_confirmation': 'any_password',
        }
    }
    sut.handle(http_request)
    add_account_stub.add.assert_called_with(
        name='any_name',
        email='any_email@mail.com',
        password='any_password',
    )


def test_should_return_500_if_EmailValidator_raises():
    sut, email_validator_stub = itemgetter('sut', 'email_validator_stub')(make_sut())
    email_validator_stub.is_valid = MagicMock(side_effect=Exception())
    http_request = {
        'body': {
            'name': 'any_name',
            'email': 'any_email@mail.com',
            'password': 'any_password',
            'password_confirmation': 'any_password',
        }
    }
    http_response = sut.handle(http_request)
    assert http_response.status_code == 500
    assert isinstance(http_response.body, ServerError)
    assert http_response.body.args[0] == 'Internal server error'


def test_should_return_500_if_AddAccount_raises():
    sut, add_account_stub = itemgetter('sut', 'add_account_stub')(make_sut())
    add_account_stub.add = MagicMock(side_effect=Exception())
    http_request = {
        'body': {
            'name': 'any_name',
            'email': 'any_email@mail.com',
            'password': 'any_password',
            'password_confirmation': 'any_password',
        }
    }
    http_response = sut.handle(http_request)
    assert http_response.status_code == 500
    assert isinstance(http_response.body, ServerError)
    assert http_response.body.args[0] == 'Internal server error'
