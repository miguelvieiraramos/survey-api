from presentation.controllers.signup import SignUpController


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
    assert http_response.get('status_code') == 400
    assert isinstance(http_response.get('body'), Exception)
    assert http_response.get('body').args[0] == 'Missing param: name'
