import jinja2

from . import config
from .requester import Requester


class Collector:
    def __init__(self):
        self.requester = Requester()
        self.requester.create_session()
        loader = jinja2.FileSystemLoader(searchpath=config.SETTINGS.jinja2_templates)
        self.template_env = jinja2.Environment(loader=loader)

    def _render_template(self, template, **kwargs):
        template = self.template_env.get_template(template)
        return template.render(**kwargs)

    def get_better_consensuses(self, symbol):
        payload = {
            "operationName": "getBetterConsensuses",
            "variables": {"symbol": symbol},
            "query": self._render_template("get_better_consensuses.j2"),
        }
        return self.requester.post_request(payload)

    def get_brokerage_actions(self, symbol):
        payload = {
            "operationName": "getBrokerageActions",
            "variables": {"symbols": [symbol]},
            "query": self._render_template("get_brokerage_actions.j2"),
        }
        return self.requester.post_request(payload)

    def get_chart_interday(self, symbol):
        payload = {
            "operationName": "getChartInterday",
            "variables": {"symbol": symbol},
            "query": self._render_template("get_chart_interday.j2"),
        }
        return self.requester.post_request(payload)

    def get_chart_intraday(self, symbol):
        payload = {
            "operationName": "getChartIntraday",
            "variables": {"symbol": symbol},
            "query": self._render_template("get_chart_intraday.j2"),
        }
        return self.requester.post_request(payload)

    def get_financial_data(self, symbol):
        payload = {
            "operationName": "getFinancialData",
            "variables": {"symbol": symbol},
            "query": self._render_template("get_financial_data.j2"),
        }
        return self.requester.post_request(payload)

    def get_market_cap(self, symbol):
        payload = {
            "operationName": "getMarketCap",
            "variables": {"symbol": symbol},
            "query": self._render_template("get_market_cap.j2"),
        }
        return self.requester.post_request(payload)

    def get_many_events(self, symbol):
        payload = {
            "operationName": "getManyEvents",
            "variables": {"symbols": [symbol]},
            "query": self._render_template("get_many_events.j2"),
        }
        return self.requester.post_request(payload)

    def get_near_events(self, symbol):
        payload = {
            "operationName": "getNearEvents",
            "variables": {"symbols": [symbol]},
            "query": self._render_template("get_near_events.j2"),
        }
        return self.requester.post_request(payload)

    def get_news_feed(self, symbol):
        payload = {
            "operationName": "getNewsFeed",
            "variables": {
                "page": 0,
                "research": False,
            },
            "query": self._render_template("get_news_feed.j2"),
        }
        return self.requester.post_request(payload)

    def get_overview_data(self, symbol):
        payload = {
            "operationName": "getOverviewData",
            "variables": {"symbol": symbol},
            "query": self._render_template("get_overview_data.j2"),
        }
        return self.requester.post_request(payload)

    def get_period_guidance(self, symbol):
        payload = {
            "operationName": "getPeriodGuidance",
            "variables": {
                "symbol": symbol,
                "start": 0,
                "end": 3,
            },
            "query": self._render_template("get_period_guidance.j2"),
        }
        return self.requester.post_request(payload)

    def get_relative_consensuses(self, symbol):
        payload = {
            "operationName": "getRelativeConsensuses",
            "variables": {
                "symbol": symbol,
                "start": 0,
                "end": 3,
            },
            "query": self._render_template("get_relative_consensuses.j2"),
        }
        return self.requester.post_request(payload)

    def get_symbol(self, symbol):
        payload = {
            "operationName": "getSymbol",
            "variables": {"symbol": symbol},
            "query": self._render_template("get_symbol.j2"),
        }
        return self.requester.post_request(payload)
