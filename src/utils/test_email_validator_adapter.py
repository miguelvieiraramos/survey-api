from unittest.mock import patch, Mock

from src.utils.email_validator_adapter import EmailValidatorAdapter


def make_sut() -> EmailValidatorAdapter:
    return EmailValidatorAdapter()


@patch('src.utils.email_validator_adapter.validators.email', Mock(return_value=False))
def test_should_return_false_if_validator_returns_false():
    sut = make_sut()
    is_valid = sut.is_valid('invalid_email@gmail.com')
    assert is_valid == False


@patch('src.utils.email_validator_adapter.validators.email', Mock(return_value=True))
def test_should_return_true_if_validator_returns_true():
    sut = make_sut()
    is_valid = sut.is_valid('valid_email@gmail.com')
    assert is_valid == True


@patch('src.utils.email_validator_adapter.validators.email')
def test_should_call_validator_with_correct_email(email_validator_mock):
    sut = make_sut()
    sut.is_valid('any_email@gmail.com')
    email_validator_mock.assert_called_once_with('any_email@gmail.com')
