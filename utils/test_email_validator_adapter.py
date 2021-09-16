from unittest.mock import patch, Mock

from utils.email_validator_adapter import EmailValidatorAdapter


@patch('utils.email_validator_adapter.validators.email', Mock(return_value=False))
def test_should_return_false_if_validator_returns_false():
    sut = EmailValidatorAdapter()
    is_valid = sut.is_valid('invalid_email@gmail.com')
    assert is_valid == False


@patch('utils.email_validator_adapter.validators.email', Mock(return_value=True))
def test_should_return_true_if_validator_returns_true():
    sut = EmailValidatorAdapter()
    is_valid = sut.is_valid('valid_email@gmail.com')
    assert is_valid == True


@patch('utils.email_validator_adapter.validators.email')
def test_should_call_validator_with_correct_email(email_validator_mock):
    sut = EmailValidatorAdapter()
    sut.is_valid('any_email@gmail.com')
    email_validator_mock.assert_called_once_with('any_email@gmail.com')
