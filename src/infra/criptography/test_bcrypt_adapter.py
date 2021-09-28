from unittest.mock import patch, Mock

import pytest

from src.infra.criptography.bcrypt_adapter import BcryptAdapter


@patch('src.infra.criptography.bcrypt_adapter.bcrypt')
def test_should_call_bcrypt_with_correct_values(mock_bcrypt):
    sut = BcryptAdapter()
    mock_bcrypt.gensalt = Mock(return_value='salt')

    sut.encrypt('any_value')
    mock_bcrypt.hashpw.assert_called_once_with(b'any_value', 'salt')


@patch('src.infra.criptography.bcrypt_adapter.bcrypt')
def test_should_return_hash_on_success(mock_bcrypt):
    sut = BcryptAdapter()
    mock_bcrypt.hashpw = Mock(return_value='hash')

    hash = sut.encrypt('any_value')

    assert hash == 'hash'


@patch('src.infra.criptography.bcrypt_adapter.bcrypt')
def test_should_raise_if_bcrypt_raises(mock_bcrypt):
    sut = BcryptAdapter()
    mock_bcrypt.hashpw = Mock(side_effect=Exception)

    with pytest.raises(Exception):
        sut.encrypt('any_value')
