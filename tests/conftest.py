from unittest import mock
import pytest

from oandapy import APIv20
from oandapy.api import Core


@pytest.fixture
def cli_oandapy():
    access_token = "945cb0accbb4c00a392bb35f1a3a4c1b-6ee340da5ac4f204ab27951077ebc43b"
    # access_token = "SECRET"
    return APIv20(environment="practice", access_token=access_token)


@pytest.fixture
def fake_client():
    access_token = 'fake-token'

    class FakeClient(Core):
        base_urls = {
            "practice": "http://example.com",
        }

    return FakeClient(environment="practice", access_token=access_token)


@pytest.fixture
def fake_session():
    get = mock.Mock(return_value=mock.Mock(status_code=200))
    post = mock.Mock(return_value=mock.Mock(status_code=201))
    delete = mock.Mock(return_value=mock.Mock(status_code=204))
    patch = mock.Mock(return_value=mock.Mock(status_code=200))
    put = mock.Mock(return_value=mock.Mock(status_code=200))

    return mock.Mock(
        get=get, post=post, put=put, patch=patch, delete=delete, headers={}
    )
