from operator import itemgetter
from unittest.mock import MagicMock

from presentation.controllers.signup import SignUpController
from presentation.errors.invalid_param_error import InvalidParamError
from presentation.errors.missing_param_error import MissingParamError
from presentation.protocols.email_validator import EmailValidator


class EmailValidatorStub(EmailValidator):
    def is_valid(self, email: str) -> bool:
        return True


def make_sut():
    email_validator_stub = EmailValidatorStub()
    return {
        'sut': SignUpController(email_validator=email_validator_stub),
        'email_validator_stub': email_validator_stub
    }


def test_should_return_400_if_no_name_is_provided():
    sut = itemgetter('sut')(make_sut())
    http_request = {
        'body': {
            'email': 'any_email',
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
            'email': 'any_email',
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
            'email': 'any_email',
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
            'email': 'any_email',
            'password': 'any_password',
            'password_confirmation': 'any_password',
        }
    }
    http_response = sut.handle(http_request)
    assert http_response.status_code == 400
    assert isinstance(http_response.body, InvalidParamError)
    assert http_response.body.args[0] == 'Invalid param: email'
