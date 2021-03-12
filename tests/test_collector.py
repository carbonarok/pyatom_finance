from unittest import TestCase

from pyatom_finance import Collector
from pyatom_finance import config


class TestCollector(TestCase):
    def setUp(self):
        config.load()
        self.collector = Collector()
        self.symbol = "CSCO"

    def test_check_symbol_exists(self):
        response = self.collector.check_symbol_exists(self.symbol)
        self.assertTrue(response)

    def test_get_better_consensuses(self):
        response = self.collector.get_better_consensuses(self.symbol)
        self.assertNotEqual(response["data"]["symbol"]["betterConsensuses"], None)

    def test_get_brokerage_actions(self):
        response = self.collector.get_brokerage_actions(self.symbol)
        self.assertNotEqual(response["data"]["symbols"][0]["brokerageActions"], None)

    def test_get_chart_interday(self):
        response = self.collector.get_chart_interday(self.symbol)
        self.assertNotEqual(response["data"]["interday"], None)

    def test_get_chart_intraday(self):
        response = self.collector.get_chart_intraday(self.symbol)
        self.assertNotEqual(response["data"]["intraday"], None)

    def test_get_financial_data(self):
        response = self.collector.get_financial_data(self.symbol)
        self.assertNotEqual(response["data"]["symbol"]["ratiosData"], None)

    def test_get_future_events(self):
        response = self.collector.get_future_events(self.symbol)
        self.assertNotEqual(response["data"]["manyEvents"]["futureEvents"], None)

    def test_get_market_cap(self):
        response = self.collector.get_market_cap(self.symbol)
        self.assertNotEqual(response["data"]["symbol"]["metric"]["atomMarketCap"], None)

    def test_get_news_feed(self):
        response = self.collector.get_news_feed(self.symbol)
        self.assertNotEqual(response["data"]["newsFeed"], None)

    def test_get_overview_data(self):
        response = self.collector.get_overview_data(self.symbol)
        self.assertNotEqual(response["data"]["symbol"], None)

    def test_get_past_events(self):
        response = self.collector.get_past_events(self.symbol)
        self.assertNotEqual(response["data"]["manyEvents"]["pastEvents"], None)

    def test_get_period_guidance(self):
        response = self.collector.get_period_guidance(self.symbol)
        self.assertNotEqual(response["data"]["symbol"]["quarterlyGuidance"], None)

    def test_get_relative_consensuses(self):
        response = self.collector.get_relative_consensuses(self.symbol)
        self.assertNotEqual(response["data"]["symbol"]["relativeConsensuses"], None)

    def test_get_symbol(self):
        response = self.collector.get_symbol(self.symbol)
        self.assertNotEqual(response["data"]["symbol"]["symbol"], None)
