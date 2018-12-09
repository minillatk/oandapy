import pytest
import status

from oandapy.exceptions import AuthError, NotFound, OandaError, ServerError
from oandapy.validators import validate_status_code


@pytest.mark.parametrize('expected,status_code,expected_exception', [
    (False, status.HTTP_401_UNAUTHORIZED, AuthError),
    (False, status.HTTP_400_BAD_REQUEST, OandaError),
    (False, status.HTTP_417_EXPECTATION_FAILED, OandaError),
    (False, status.HTTP_404_NOT_FOUND, NotFound),
    (False, status.HTTP_500_INTERNAL_SERVER_ERROR, ServerError),
])
def test_validate_status_invalid(expected, status_code, expected_exception):
    is_valid, exception_class = validate_status_code(status_code, None)
    assert is_valid == expected
    assert type(exception_class) == expected_exception


def test_validate_status_valid(fake_client):
    is_valid, exception_class = validate_status_code(status.HTTP_200_OK, None)
    assert is_valid
    assert not exception_class
