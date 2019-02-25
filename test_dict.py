from run import create_app


def test_status_code():
    app = create_app()
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_five_items():
    app = create_app()
    client = app.test_client()
    response = client.get('/?word=a')
    json_data = response.get_json()
    assert len(json_data['results']) == 6


def test_page_with_words():
    app = create_app()
    client = app.test_client()
    response = client.get('/?word=a')
    assert response.status_code == 200


def test_page_with_no_words():
    app = create_app()
    client = app.test_client()
    response = client.get('/?word=')
    assert response.status_code == 200


def test_null_word_returns_null():
    app = create_app()
    client = app.test_client()
    response = client.get('/?word=')
    json_data = response.get_json()
    message = json_data['results']
    assert message == ''
