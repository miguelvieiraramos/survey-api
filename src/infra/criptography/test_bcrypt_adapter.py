from unittest.mock import patch

from src.infra.criptography.bcrypt_adapter import BcryptAdapter


@patch('src.infra.criptography.bcrypt_adapter.bcrypt.hashpw')
def test_should_call_bcrypt_with_correct_values(mock_bcrypt):
    salt = 12
    sut = BcryptAdapter(salt)
    sut.encrypt('any_value')
    mock_bcrypt.assert_called_once_with(b'any_value', 12)
