import pytest

from cuve.order_service import application_factory

@pytest.fixture
def client(loop, test_client):
    app = application_factory()
    client = test_client(app)
    return loop.run_until_complete(client)
