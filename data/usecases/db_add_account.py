from data.protocols.encrypter import Encrypter
from domain.models.account import AccountModel
from domain.usecases.add_account import AddAccountModel, AddAccount


class DbAddAccount(AddAccount):

    def __init__(self, encrypter: Encrypter):
        self.encrypter = encrypter

    def add(self, account: AddAccountModel) -> AccountModel:
        self.encrypter.encrypt(account.password)
