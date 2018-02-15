
def test_login(client):
    resp = client.post('/api/v1.0/auth/login')
    assert resp.status_code == 200, f'Invalid response code. {resp}'

def test_logut(client):
    resp = client.post('/api/v1.0/auth/logout')
    assert resp.status_code == 200, f'Invalid response code. {resp}'
