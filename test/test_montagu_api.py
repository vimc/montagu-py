from src.montagu_api import MontaguAPI
import pytest

base_url = 'http://localhost:8080'
user = 'test.user@example.com'
password = 'password'


def test_init():
    api = MontaguAPI(base_url, user, password)
    assert len(api.token) > 0


def test_error_on_incorrect_credentials():
    with pytest.raises(Exception) as ex:
        MontaguAPI(base_url, user, 'wrong password')
    assert(ex.value.message == 'Unexpected status code: 401. Unable to authenticate.')


def test_diseases():
    api = MontaguAPI(base_url, user, password)
    diseases = api.diseases()
    assert len(diseases) == 1
    disease = diseases[0]
    assert disease['id'] == 'YF'
    assert disease['name'] == 'Yellow Fever'
