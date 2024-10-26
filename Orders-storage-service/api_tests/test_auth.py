import pytest
from requests.exceptions import HTTPError

def test_adfs_authenticate_success(adfs_token, requests_mock):
    # Данные для теста
    client_id = 'test-client-id'
    client_secret = 'test-client-secret'
    resource = 'test-resource'
    adfs_url = 'https://test-adfs-url/adfs/oauth2/token'
    username = 'testuser'
    password = 'testpassword'
    
    # Имитация успешного ответа от ADFS
    requests_mock.post(adfs_url, json={'access_token': 'test-access-token'}, status_code=200)
    
    # Использование фикстуры для получения токена
    token = adfs_token(client_id, client_secret, resource, adfs_url, username, password)
    
    # Проверка, что токен вернулся корректно
    assert token == 'test-access-token'

def test_adfs_authenticate_failure(adfs_token, requests_mock):
    # Данные для теста
    client_id = 'test-client-id'
    client_secret = 'test-client-secret'
    resource = 'test-resource'
    adfs_url = 'https://test-adfs-url/adfs/oauth2/token'
    username = 'testuser'
    password = 'testpassword'
    
    # Имитация неуспешного ответа от ADFS
    requests_mock.post(adfs_url, status_code=401, json={'error': 'invalid_grant'})
    
    # Проверка, что выбрасывается ошибка при неуспешной аутентификации
    with pytest.raises(HTTPError):
        adfs_token(client_id, client_secret, resource, adfs_url, username, password)

def test_login_success(api_client):
    """Тест успешной авторизации на /api/v2/auth/login."""
    response = api_client("/api/v2/auth/login", method="get", params={"source": "http://example.com/success"})
    assert response.status_code == 200
    assert "token" in response.json(), "В ответе отсутствует токен"

def test_logout_success(api_client):
    """Тест успешного выхода на /api/v2/auth/logout."""
    response = api_client("/api/v2/auth/logout", method="get", params={"source": "http://example.com/logout"})
    assert response.status_code == 200
    assert "message" in response.json(), "В ответе отсутствует подтверждение выхода"

def test_refresh_token(api_client):
    """Тест успешного обновления JWT-токена на /api/v2/auth/refresh."""
    data = {"refresh_token": "sample_refresh_token"}
    response = api_client("/api/v2/auth/refresh", method="post", data=data)
    assert response.status_code == 200
    assert "new_token" in response.json(), "В ответе отсутствует новый токен"

