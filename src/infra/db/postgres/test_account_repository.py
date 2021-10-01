from src.domain.models.account import AccountModel
from src.domain.usecases.add_account import AddAccountModel
from src.infra.db.postgres.account_repository import AccountRepository
from src.infra.db.postgres.postgres_helper import PostgresHelper


def setup_module():
    PostgresHelper.URI['database'] = 'test'
    PostgresHelper.init_db()


def teardown_module():
    PostgresHelper.close_db()


def test_should_return_an_account_on_success():
    sut = AccountRepository()
    account: AccountModel = sut.add(AddAccountModel(
        name='any_name',
        email='any_email@mail.com',
        password='any_password'
    ))
    assert account
    assert account.id
    assert account.name == 'any_name'
    assert account.email == 'any_email@mail.com'
    assert account.password == 'any_password'
