from abc import ABC, abstractmethod

from domain.models.account import AccountModel


class AddAccount(ABC):

    @abstractmethod
    def add(self, name: str, email: str, password: str) -> AccountModel:
        pass
