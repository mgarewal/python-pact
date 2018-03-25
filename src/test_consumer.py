import atexit

from src.consumer import get_status_code


from pact import Consumer, Provider


pact = Consumer('consumer').has_pact_with(Provider('provider'))
pact.start_service()
atexit.register(pact.stop_service)


def test_client():
    url = 'http://localhost:1234'
    pact.given(
        'a url'
    ).upon_receiving(
        'a request to that url'
    ).with_request(
        'get',
        '/'
    ).will_respond_with(200)

    with pact:
        assert get_status_code(url)