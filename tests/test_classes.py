# -*- coding: utf-8 -*-

'''
test_classes
------------

tests `stockbot.classes` module
'''

import datetime as dt
from decimal import Decimal
import unittest

from dateutil.tz import tzlocal
import pytz

from stockbot.classes import (MarketData)


class TestMarketData(unittest.TestCase):

    def setUp(self):
        self.data_in = {'symbol': 'SPY',
                        'last': '188.01',
                        'date': '9/28/2015',
                        'time': '4:23pm',
                        'change': '-4.84',
                        'open': '191.78',
                        'high': '191.91',
                        'low': '187.64',
                        'volume': '178515871'}

    def test_MarketData(self):
        a = MarketData(self.data_in)
        b = {
            'high': 191.91,
            'last': 188.01,
            'symbol': 'SPY',
            'volume': 178515871,
            'low': 187.64,
            'time': dt.datetime.combine(dt.datetime.today().date(), dt.time(16, 23)),
            'date': dt.datetime(2015, 9, 28, 0, 0),
            'open': 191.78,
            'change': -4.84,
        }
        self.assertEqual(a, b)

    def test_MarketData_decimal(self):
        a = MarketData(self.data_in, decimal=True)
        b = {
            'high': Decimal('191.91'),
            'last': Decimal('188.01'),
            'symbol': 'SPY',
            'volume': Decimal('178515871'),
            'low': Decimal('187.64'),
            'time': dt.datetime.combine(dt.datetime.today().date(), dt.time(16, 23)),
            'date': dt.datetime(2015, 9, 28, 0, 0),
            'open': Decimal('191.78'),
            'change': Decimal('-4.84'),
        }
        self.assertEqual(a, b)

    def test_MarketData_clean_dt(self):
        a = MarketData(self.data_in).clean_dt()
        b = {
            'high': 191.91,
            'last': 188.01,
            'symbol': 'SPY',
            'volume': 178515871,
            'low': 187.64,
            'open': 191.78,
            'change': -4.84,
            'datetime': dt.datetime(2015, 9, 28, 20, 23, tzinfo=pytz.timezone('UTC'))
        }
        self.assertEqual(a, b)

    def tearDown(self):
        pass
