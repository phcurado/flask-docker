import json

create_attrs = dict(
    username='paulo_curado',
    email='paulo_curado@email.com',
    phone='1112344321',
    address = [
        dict(
            street='Street 1',
            number='1'
        ),
        dict(
            street='Street 2',
            number='2'
        )
    ]
)

update_attrs = dict(
    username='paulo_curado_1',
    email='paulo_curado_1@email.com',
    phone='1112344322',
        address = [
        dict(
            id=1,
            street='Street 11',
            number='11'
        ),
        dict(
            street='Street 21',
            number='21'
        )
    ]
)

def test_404_route(client):
    """404 route"""
    resp = client.get('/generic_route')
    assert resp.status_code == 404

def test_list_user(client):
    """List users"""
    resp = client.get('/api/users')

    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert data['data'] == []

def test_show_empty_user(client):
    """List users"""
    resp = client.get('/api/users/1')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404

def test_create_user(client):
    """Create user"""
    user_params = json.dumps(create_attrs)
    resp = client.post('/api/users', data = user_params, content_type='application/json')
    
    data = json.loads(resp.data.decode())
    
    assert resp.status_code == 201
    assert data['username'] == 'paulo_curado'
    assert data['email'] == 'paulo_curado@email.com'
    assert data['phone'] == '1112344321'
    assert data['address'][0]['street'] == 'Street 1'
    assert data['address'][0]['number'] == 1
    assert data['address'][1]['street'] == 'Street 2'
    assert data['address'][1]['number'] == 2


def test_show_user(client):
    """List users"""
    resp = client.get('/api/users/1')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert data['username'] == 'paulo_curado'
    assert data['email'] == 'paulo_curado@email.com'
    assert data['address'][0]['street'] == 'Street 1'
    assert data['address'][0]['number'] == 1
    assert data['address'][1]['street'] == 'Street 2'
    assert data['address'][1]['number'] == 2

def test_update_user(client):
    """Update user"""
    user_params = json.dumps(update_attrs)
    resp = client.put('/api/users/1', data = user_params, content_type='application/json')
    
    data = json.loads(resp.data.decode())

    assert resp.status_code == 201
    assert data['username'] == 'paulo_curado_1'
    assert data['email'] == 'paulo_curado_1@email.com'
    assert len(data['address']) == 2
    assert data['address'][0]['street'] == 'Street 11'
    assert data['address'][0]['number'] == 11
    assert data['address'][1]['street'] == 'Street 21'
    assert data['address'][1]['number'] == 21

def test_delete_user(client):
    """Delete user"""
    user_params = json.dumps(update_attrs)
    resp = client.delete('/api/users/1', content_type='application/json')
    assert resp.status_code == 204