import json
from unittest.mock import Mock

import pytest
from requests.exceptions import Timeout, ReadTimeout, ConnectionError as RequestsConnectionError

from oandapy.api import Core
from oandapy.exceptions import EnvironmentNotFound, ServerError


@pytest.fixture
def url_base():
    return 'http://example.com/v3/'


@pytest.fixture
def endpoint():
    return 'fake/endpoint'


def test_get_environment_error(fake_client):
    class Test(Core):
        pass

    with pytest.raises(EnvironmentNotFound) as error:
        Test("INVALID", access_token='FAKE')

    assert str(error.value) == "Environment 'INVALID' does not exist!"


def test_sync_with_server_error(fake_client, endpoint):
    fake_client.make_request = Mock(side_effect=ServerError('foo'))

    with pytest.raises(ServerError) as error:
        fake_client.search(endpoint)

    assert str(error.value) == 'OANDA server returned a internal server error'


@pytest.mark.parametrize('exception', [
    Timeout, ReadTimeout, RequestsConnectionError,
])
def test_sync_with_requests_error(fake_client, endpoint, exception):
    fake_client.transport.make_request = Mock(side_effect=exception('foo'))

    with pytest.raises(ServerError) as error:
        fake_client.search(endpoint)

    assert str(error.value) == 'OANDA server returned a internal server error'


def test_sync_search(fake_client, fake_session, endpoint, url_base):
    fake_client.transport.session = fake_session
    fake_client.search(endpoint)
    assert fake_session.get.called
    assert fake_session.get.call_args[0][0] == url_base + endpoint
    assert fake_session.get.call_args[1]['params'] == {}


def test_sync_search_with_params(fake_client, fake_session, endpoint, url_base):
    fake_client.transport.session = fake_session
    fake_client.search(endpoint, params={'status': 'open'})
    assert fake_session.get.called
    assert fake_session.get.call_args[0][0] == url_base + endpoint
    assert fake_session.get.call_args[1]['params'] == {'status': 'open'}


def test_sync_create(fake_client, fake_session, endpoint, url_base):
    fake_client.transport.session = fake_session
    payload = {
        "order": {
            "units": "100",
            "instrument": "EUR_USD",
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
        }
    }
    fake_client.create(endpoint, data=payload)
    assert fake_session.post.called
    assert fake_session.post.call_args[0][0] == url_base + endpoint
    assert fake_session.post.call_args[1]['data'] == json.dumps(payload)


def test_sync_update_with_put(fake_client, fake_session, endpoint, url_base):
    fake_client.transport.session = fake_session
    payload = {
        "order": {
            "timeInForce": "GTC",
            "price": "1.7000",
            "type": "TAKE_PROFIT",
            "tradeID": "6368"
        }
    }
    fake_client.update(endpoint + '6368', data=payload)
    assert fake_session.put.called
    assert fake_session.put.call_args[0][0] == url_base + endpoint + '6368'
    assert fake_session.put.call_args[1]['data'] == json.dumps(payload)


def test_sync_update_with_patch(fake_client, fake_session, endpoint, url_base):
    fake_client.transport.session = fake_session
    payload = {'instrument': 'EUR_USD'}
    fake_client.update(endpoint + '1234', data=payload, partial=True)
    assert fake_session.patch.called
    assert fake_session.patch.call_args[0][0] == url_base + endpoint + '1234'
    assert fake_session.patch.call_args[1]['data'] == json.dumps(payload)
