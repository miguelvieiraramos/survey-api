from unittest.mock import Mock

import pytest

from data.protocols.add_account_repository import AddAccountRepository
from data.protocols.encrypter import Encrypter
from data.usecases.db_add_account import DbAddAccount
from domain.models.account import AccountModel
from domain.usecases.add_account import AddAccountModel


class EncrypterStub(Encrypter):

    def encrypt(self, value: str) -> str:
        return 'hashed_password'


class AddAccountRepositoryStub(AddAccountRepository):

    def add(self, account_data: AddAccountModel) -> AccountModel:
        return AccountModel(
            id='valid_id',
            name='valid_name',
            email='valid_email',
            password='valid_password'
        )


def make_sut():
    encrypter_stub = EncrypterStub()
    add_account_repository_stub = AddAccountRepositoryStub()
    return DbAddAccount(encrypter_stub, add_account_repository_stub), encrypter_stub, add_account_repository_stub


def test_should_call_encrypter_with_correct_password():
    sut, encrypter_stub, _ = make_sut()
    encrypter_stub.encrypt = Mock()
    account_data = AddAccountModel(
        name='valid_name',
        email='valid_email',
        password='valid_password'
    )
    sut.add(account_data)
    encrypter_stub.encrypt.assert_called_once_with('valid_password')


def test_should_raise_if_encrypter_raises():
    sut, encrypter_stub, _ = make_sut()
    encrypter_stub.encrypt = Mock()
    encrypter_stub.encrypt.side_effect = Exception
    account_data = AddAccountModel(
        name='valid_name',
        email='valid_email',
        password='valid_password'
    )

    with pytest.raises(Exception):
        sut.add(account_data)


def test_should_call_AddAccountRepository_with_correct_params():
    sut, _, add_account_repository_stub = make_sut()
    add_account_repository_stub.add = Mock()
    account_data = AddAccountModel(
        name='valid_name',
        email='valid_email',
        password='valid_password'
    )
    sut.add(account_data)
    add_account_repository_stub.add.assert_called_once_with(
        AddAccountModel(name='valid_name',  email='valid_email', password='hashed_password')
    )
