import pytest
import requests

BASE_URL = "http://orders-storage-service.staging.dostaevsky.ru"

@pytest.fixture
def adfs_token():
    """
    Фикстура для получения токена авторизации через ADFS.

    :return: Функция для выполнения запроса токена ADFS.
    """
    def authenticate(client_id, client_secret, resource, adfs_url, username, password):
        """
        Аутентификация через ADFS с использованием OAuth2.

        :param client_id: Идентификатор клиента (приложения).
        :param client_secret: Секрет клиента.
        :param resource: Ресурс, к которому требуется доступ (например, URI API).
        :param adfs_url: URL вашего ADFS сервера для токена.
        :param username: Имя пользователя (логин).
        :param password: Пароль.
        :return: Токен доступа (access token), если аутентификация прошла успешно.
        """
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'resource': resource,
            'grant_type': 'password',
            'username': username,
            'password': password,
            'scope': 'openid'
        }

        response = requests.post(adfs_url, data=data)
        
        if response.status_code == 200:
            return response.json().get('access_token')
        else:
            response.raise_for_status()

    return authenticate


@pytest.fixture
def api_client():
    """Возвращает функцию для отправки HTTP-запросов к API."""
    def client(endpoint, method="get", data=None, params=None, headers=None):
        url = f"{BASE_URL}{endpoint}"
        response = requests.request(method, url, json=data, params=params, headers=headers)
        return response
    return client