from utils.email_validator_adapter import EmailValidatorAdapter


def test_should_return_false_if_validator_returns_false():
    sut = EmailValidatorAdapter()
    is_valid = sut.is_valid('invalid_email@gmail.com')
    assert is_valid == False
