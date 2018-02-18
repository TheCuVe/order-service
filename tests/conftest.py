import pytest
import factory

from cuve.order_service.db import transaction, tables
from cuve.order_service.app import application_factory
from cuve.order_service.config import load_config, ConfigSchema


def pytest_addoption(parser):
    parser.addoption('--config', action="store",
                     default='./etc/config/development.yml')


@pytest.fixture
def client(request, loop, test_client):
    config = load_config(ConfigSchema, request.config.getoption('--config'))
    app = application_factory(config, loop)
    client = test_client(app)
    return loop.run_until_complete(client)


@pytest.fixture
def app(client):
    """ Shortcut for accessing application behind test client
    """
    return client.server.app


@pytest.fixture(autouse=True, scope='function')
def transaction_auto_rollback(app):
    """ Autoused fixture creating savepoint before every
    test and rollbacking changes after test finishes
    """
    pass

#
# Facories for fake table records
#


@pytest.fixture
def company_factory(app):
    """ Create fake company
    """
    class CompanyFactory(factory.Factory):
        name = factory.Faker('company')
        phone = factory.Faker('phone')
        description = factory.Faker('bs')

    async def factory(*args, **kwargs):
        fake = CompanyFactory.stub(*args, **kwargs)
        ins_stmt = tables.company.insert().values(**fake.__dict__)
        async with transaction(app) as trans:
            company_id = await trans.connection.scalar(ins_stmt)
            await trans.commit()
            sel_stmt = tables.company.select().where(
                tables.company.id == company_id)
            select_result = await trans.connection.execture(sel_stmt)
            return await select_result.fetch_one()

    return factory


@pytest.fixture
def account(app, company):
    """ Create fake user account
    """
    pass


@pytest.fixture
def software(app, company):
    """ Create fake software
    """
    pass


@pytest.fixture
def software_order(app, account):
    """ Create fake software order
    """
    pass
