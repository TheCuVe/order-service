
async def test_login(client):
    resp = await client.post('/api/v1.0/auth/login')
    assert resp.status == 200, f'Invalid response code. {resp}'

async def test_logut(client):
    resp = await client.post('/api/v1.0/auth/logout')
    assert resp.status == 200, f'Invalid response code. {resp}'
