from src.montagu_api import MontaguAPI


def test_init():
    api = MontaguAPI('http://localhost:8080', 'test.user@example.com', 'password')
    assert len(api.token) > 0
    # TODO Get something innocuous from API to prove the token works!