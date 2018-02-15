import pytest

from cuve.order_service.app import application_factory
from cuve.order_service.config import load_config, ConfigSchema

@pytest.fixture
def client(request, loop, test_client):
    config = load_config(ConfigSchema, './etc/config/development.yml')
    app = application_factory(config, loop)
    client = test_client(app)
    return loop.run_until_complete(client)
