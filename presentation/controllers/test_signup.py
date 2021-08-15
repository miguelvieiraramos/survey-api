from presentation.controllers.signup import SignUpController
from presentation.errors.missing_param_error import MissingParamError


def test_should_return_400_if_no_name_is_provided():
    sut = SignUpController()
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
    sut = SignUpController()
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
    sut = SignUpController()
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
    sut = SignUpController()
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
