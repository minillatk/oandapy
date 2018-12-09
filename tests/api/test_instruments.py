from oandapy import APIv20
from oandapy.api import Instrument

from ..vcr_conf import vcr


def test_instruments__with_valid_client(cli_oandapy):
    con = APIv20(access_token='TEST')
    assert isinstance(con.instrument, Instrument)


@vcr.use_cassette
def test_instruments_get_candles_with_instrument_only(cli_oandapy):
    instrument = 'EUR_USD'
    result = cli_oandapy.instrument.get_candles(instrument).as_dict()
    assert 'candles' in result
    assert result['instrument'] == instrument


@vcr.use_cassette
def test_instruments_get_candles_with_period_and_params(cli_oandapy):
    instrument = 'EUR_USD'
    kwargs = {
        'from_date': '2018-12-05',
        'to_date': '2018-12-08',
        'granularity': 'M1',
        'price': 'A'
    }
    result = cli_oandapy.instrument.get_candles(instrument, **kwargs).as_dict()

    assert 'candles' in result
    assert result['instrument'] == instrument


@vcr.use_cassette
def test_instruments_get_orderbook_with_instrument_only(cli_oandapy):
    instrument = 'EUR_USD'
    result = cli_oandapy.instrument.get_orderbook(instrument).as_dict()
    assert 'orderBook' in result
    assert 'buckets' in result['orderBook']
    assert result['orderBook']['instrument'] == instrument


@vcr.use_cassette
def test_instruments_get_orderbook_time(cli_oandapy):
    instrument = 'EUR_USD'
    time = '2018-11-07T04:20:00Z'
    result = cli_oandapy.instrument.get_orderbook(instrument, time=time).as_dict()
    assert 'orderBook' in result
    assert 'buckets' in result['orderBook']
    assert result['orderBook']['instrument'] == instrument


@vcr.use_cassette
def test_instruments_get_positionbook_with_instrument_only(cli_oandapy):
    instrument = 'EUR_USD'
    result = cli_oandapy.instrument.get_positionbook(instrument).as_dict()
    assert 'positionBook' in result
    assert 'buckets' in result['positionBook']
    assert result['positionBook']['instrument'] == instrument


@vcr.use_cassette
def test_instruments_get_positionbook_with_time(cli_oandapy):
    instrument = 'EUR_USD'
    time = '2018-11-07T04:20:00Z'
    result = cli_oandapy.instrument.get_positionbook(instrument, time=time).as_dict()
    assert 'positionBook' in result
    assert 'buckets' in result['positionBook']
    assert result['positionBook']['instrument'] == instrument
