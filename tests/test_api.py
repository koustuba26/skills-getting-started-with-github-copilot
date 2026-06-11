def test_get_activities(client):
    # Arrange: client fixture provides a clean app state
    # Act
    res = client.get('/activities')
    # Assert
    assert res.status_code == 200
    data = res.json()
    assert 'Chess Club' in data
    assert isinstance(data['Chess Club']['participants'], list)


def test_signup_success(client):
    # Arrange
    activity = 'Chess Club'
    email = 'newstudent@mergington.edu'
    # Act
    res = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert res.status_code == 200
    assert email in client.get('/activities').json()[activity]['participants']


def test_signup_duplicate(client):
    # Arrange
    activity = 'Chess Club'
    email = 'michael@mergington.edu'
    # Act
    res = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert res.status_code == 400


def test_signup_not_found(client):
    # Arrange
    activity = 'Nonexistent Club'
    email = 'noone@nowhere.edu'
    # Act
    res = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert res.status_code == 404


def test_unregister_success(client):
    # Arrange
    activity = 'Chess Club'
    email = 'daniel@mergington.edu'
    # Act
    res = client.delete(f"/activities/{activity}/participants?email={email}")
    # Assert
    assert res.status_code == 200
    assert email not in client.get('/activities').json()[activity]['participants']


def test_unregister_not_found(client):
    # Arrange
    activity = 'Chess Club'
    email = 'ghost@nowhere.edu'
    # Act
    res = client.delete(f"/activities/{activity}/participants?email={email}")
    # Assert
    assert res.status_code == 404


def test_root_redirect(client):
    # Arrange
    # Act
    res = client.get('/', follow_redirects=False)
    # Assert
    assert res.status_code in (307, 302)
    assert '/static/index.html' in res.headers.get('location', '')
