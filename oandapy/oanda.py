# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Oanda API Library
"""

from .api.oanda_base import Core
from .exceptions.exceptions import OandaError
import sys

from .api.account import Account
from .api.orders import Orders
from .api.positions import Positions
from .api.pricing import Pricing
from .api.trades import Trades
from .api.transactions import Transactions


class APIv20(Core):
    """Oanda REST API v20 Class

    This class instanciates all endpoint classes for you
    """

    def __init__(self, environment="practice", access_token=None, headers=None):
        """Instantiates an instance of Oanda REST API class

        Args:
            environment: A string providing de environment for OANDA's API.
            access_token: An optional string variable that specifies the access
                token.
            headers: An optional dict of parameters (Default: None)
        """
        super(APIv20, self).__init__(environment, access_token, headers)
        self._version = "v3"

        self.account = Account(self)
        self.orders = Orders(self)
        self.positions = Positions(self)
        self.pricing = Pricing(self)
        self.trades = Trades(self)
        self.transactions = Transactions(self)