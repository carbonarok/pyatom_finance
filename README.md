# Atom Finance for Python

## Install

### Pip

`pip install pyatom_finance`

### Poetry

1) Clone repository
2) Change directory to project root
3) Run `poetry install`

## Usage

### Configuration

Configure username and password for Atom finance using one of the two methods:

1) Set username and password in pyproject.toml

``` pyproject.toml
[tool.atom_finance]
username="[username]"
password="[password]"
```

2) Configure using config pydantic.

``` python
from pyatom_finance import config
config.load()
config.SETTINGS.username = "[username]"
config.SETTINGS.password = "[password]"
```

### Using Collector

1) Import collector class `from pyatom_finance import Collector`.
2) Initialize collector class `collector = Collector()`.
3) Start using data collection functions.

### Example

``` python
from pyatom_finance import Collector
from pyatom_finance import config


config.load()
config.SETTINGS.username = "[username]"
config.SETTINGS.password = "[password]"
collector = Collector()
print(collector.check_symbol_exists("CSCO"))
print(collector.get_better_consensuses("CSCO"))
print(collector.get_brokerage_actions("CSCO"))
print(collector.get_chart_interday("CSCO"))
print(collector.get_chart_intraday("CSCO"))
print(collector.get_financial_data("CSCO"))
print(collector.get_future_events("CSCO"))
print(collector.get_market_cap("CSCO"))
print(collector.get_many_events("CSCO"))
print(collector.get_near_events("CSCO"))
print(collector.get_news_feed("CSCO"))
print(collector.get_overview_data("CSCO"))
print(collector.get_past_events("CSCO"))
print(collector.get_period_guidance("CSCO"))
print(collector.get_relative_consensuses("CSCO"))
print(collector.get_symbol("CSCO"))
```
