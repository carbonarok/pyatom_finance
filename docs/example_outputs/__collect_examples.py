"""Collect data examples"""
import json

from pyatom_finance import Collector
from pyatom_finance import config


SYMBOL = "CSCO"

config.load()
collector = Collector()


def write_json(name, output):
    """Write dictionaries to JSON file"""
    with open(f"./{name}.json", "w+") as file:
        file.write(
            json.dumps(
                output,
                indent=4,
            )
        )


write_json("get_better_consensuses", collector.get_better_consensuses(SYMBOL))
write_json("get_brokerage_actions", collector.get_brokerage_actions(SYMBOL))
write_json("get_chart_interday", collector.get_chart_interday(SYMBOL))
write_json("get_chart_intraday", collector.get_chart_intraday(SYMBOL))
write_json("get_financial_data", collector.get_financial_data(SYMBOL))
write_json("get_market_cap", collector.get_market_cap(SYMBOL))
write_json("get_many_events", collector.get_many_events(SYMBOL))
write_json("get_near_events", collector.get_near_events(SYMBOL))
write_json("get_news_feed", collector.get_news_feed(SYMBOL))
write_json("get_overview_data", collector.get_overview_data(SYMBOL))
write_json("get_period_guidance", collector.get_period_guidance(SYMBOL))
write_json("get_relative_consensuses", collector.get_relative_consensuses(SYMBOL))
write_json("get_symbol", collector.get_symbol(SYMBOL))
