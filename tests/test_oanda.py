#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Test functions for oanda module
"""

import unittest
from unittest import mock
from oanda_api import oanda


class TestOandaApi(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        a = oanda.APIv20(access_token="test")

    def tearDown(self):
        pass

    def test_name(self):
        pass