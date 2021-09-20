from abc import ABC, abstractmethod

from src.domain.models.account import AccountModel
from src.domain.usecases.add_account import AddAccountModel


class AddAccountRepository(ABC):

    @abstractmethod
    def add(self, account_data: AddAccountModel) -> AccountModel:
        pass
