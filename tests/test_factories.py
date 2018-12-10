from oandapy.factories import ResponseFactory


def test_response_factory():
    data = {'accounts': [{'id': '000-000-0000000-000', 'tags': []}]}

    class ResponseTest:
        def json(self):
            return data

    account_id = data['accounts'][0]['id']
    response = ResponseFactory(ResponseTest(), 'data/test')
    assert response.as_dict() == data

    obj = response.as_obj()
    assert obj.accounts[0].id == account_id
    assert '<DataTest object>' == str(response)
