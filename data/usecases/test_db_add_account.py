from unittest.mock import Mock

import pytest

from data.usecases.db_add_account import DbAddAccount
from domain.usecases.add_account import AddAccountModel


class EncrypterStub:

    def encrypt(self, value: str) -> str:
        return 'hashed_password'


def make_sut():
    encrypter_stub = EncrypterStub()
    return DbAddAccount(encrypter_stub), encrypter_stub


def test_should_call_encrypter_with_correct_password():
    sut, encrypter_stub = make_sut()
    encrypter_stub.encrypt = Mock()
    account_data = AddAccountModel(
        name='valid_name',
        email='valid_email',
        password='valid_password'
    )
    sut.add(account_data)
    encrypter_stub.encrypt.assert_called_once_with('valid_password')


def test_should_raise_if_encrypter_raises():
    sut, encrypter_stub = make_sut()
    encrypter_stub.encrypt = Mock()
    encrypter_stub.encrypt.side_effect = Exception
    account_data = AddAccountModel(
        name='valid_name',
        email='valid_email',
        password='valid_password'
    )

    with pytest.raises(Exception):
        sut.add(account_data)
