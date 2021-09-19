from data.protocols.add_account_repository import AddAccountRepository
from data.protocols.encrypter import Encrypter
from domain.models.account import AccountModel
from domain.usecases.add_account import AddAccountModel, AddAccount


class DbAddAccount(AddAccount):

    def __init__(self, encrypter: Encrypter, add_account_repository: AddAccountRepository):
        self.encrypter = encrypter
        self.add_account_repository = add_account_repository

    def add(self, account_data: AddAccountModel) -> AccountModel:
        hashed_password = self.encrypter.encrypt(account_data.password)
        self.add_account_repository.add(
            AddAccountModel(name=account_data.name, email=account_data.email, password=hashed_password)
        )
