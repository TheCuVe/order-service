import json


async def test_create_order(client):
    """ Creating basic order and retrieving id
    """
    result = await client.post('/api/v1/orders/')
    assert result.status == 200, f'Invalid response code: {result}'
    payload = json.loads(await result.text())
    assert 'order_id' in payload
