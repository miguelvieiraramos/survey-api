from src.domain.models.account import AccountModel
from src.domain.usecases.add_account import AddAccountModel
from src.infra.db.postgres.postgres_helper import PostgresHelper


class AccountRepository:

    def add(self, account_data: AddAccountModel) -> AccountModel:
        account = PostgresHelper.one(
            'INSERT INTO account (name, email, password) VALUES (%s, %s, %s) RETURNING id, name, email, password',
            (account_data.name, account_data.email, account_data.password)
        )
        return AccountModel(
            id=account[0][0],
            name=account[0][1],
            email=account[0][2],
            password=account[0][3]
        )

