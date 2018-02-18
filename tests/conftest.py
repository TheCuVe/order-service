import pytest

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
