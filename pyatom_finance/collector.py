from .requester import Requester


class Collector:
    def __init__(self):
        self.requester = Requester()
        self.requester.create_session()

    def get_better_consensuses(self, symbol):
        payload = {
            "operationName": "getBetterConsensuses",
            "variables": {"symbol": symbol},
            "query": "query getBetterConsensuses($symbol: String!) {\n  symbol(symbol: $symbol) {\n    id\n    currentFY\n    currentFQ\n    sectorType\n    betterConsensuses {\n      id\n      fq\n      fy\n      isActual\n      dateHeld\n      datePeriodEnds\n      ...HistoricalData\n      __typename\n    }\n    recommendationConsensuses {\n      NumberOfStrongBuy\n      NumberOfBuy\n      NumberOfHold\n      NumberOfSell\n      NumberOfStrongSell\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment HistoricalData on BetterConsensus {\n  REV\n  EBIT\n  Atom__EBITDA\n  EPS\n  TBVPS\n  BVPS\n  __typename\n}\n",
        }
        return self.requester.post_request(payload)

    def get_brokerage_actions(self, symbol):
        payload = {
            "operationName": "getBrokerageActions",
            "variables": {"symbols": [symbol]},
            "query": "query getBrokerageActions($symbols: [String]!) {\n  symbols(symbols: $symbols) {\n    symbol\n    brokerageActions {\n      action\n      actionType\n      oldActionType\n      brokerageName\n      date\n      oldTargetPrice\n      targetPrice\n      __typename\n    }\n    guidanceActions {\n      period\n      periodYear\n      currency\n      benzingaUpdated\n      ...GuidanceData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment GuidanceData on Guidance {\n  adjEpsMax\n  adjEpsMin\n  gaapEpsMax\n  gaapEpsMin\n  adjEpsPriorMax\n  adjEpsPriorMin\n  gaapEpsPriorMax\n  gaapEpsPriorMin\n  adjRevenueMax\n  adjRevenueMin\n  gaapRevenueMax\n  gaapRevenueMin\n  adjRevenuePriorMax\n  adjRevenuePriorMin\n  gaapRevenuePriorMax\n  gaapRevenuePriorMin\n  __typename\n}\n",
        }
        return self.requester.post_request(payload)

    def get_chart_interday(self, symbol):
        payload = {
            "operationName": "getChartInterday",
            "variables": {"symbol": symbol},
            "query": "query getChartInterday($symbol: String!, $chartType: String, $rangeUnit: String, $rangeCount: Int) {\n  interday(symbol: $symbol, chartType: $chartType, rangeUnit: $rangeUnit, rangeCount: $rangeCount) {\n    date\n    price\n    volume\n    changePercent\n    open\n    close\n    high\n    low\n    __typename\n  }\n}\n",
        }
        return self.requester.post_request(payload)

    def get_chart_intraday(self, symbol):
        payload = {
            "operationName": "getChartIntraday",
            "variables": {"symbol": symbol},
            "query": "query getChartIntraday($symbol: String!, $chartType: String, $rangeCount: Int) {\n  intraday(symbol: $symbol, chartType: $chartType, rangeCount: $rangeCount) {\n    date\n    price\n    volume\n    marketStatus\n    open\n    close\n    high\n    low\n    __typename\n  }\n}\n",
        }
        return self.requester.post_request(payload)

    def get_financial_data(self, symbol):
        payload = {
            "operationName": "getFinancialData",
            "variables": {"symbol": symbol},
            "query": "query getFinancialData($symbol: String!) {\n  symbol(symbol: $symbol) {\n    symbol\n    id\n    ratiosData {\n      reportingCurrency\n      currencySymbol\n      __typename\n    }\n    financialTabData {\n      Annual {\n        periodEndDate\n        fiscalYear\n        periodType\n        periodLength\n        periodUnit\n        incomeStatement {\n          source\n          periodLength\n          periodUnit\n          updateType\n          statementDate\n          auditorName\n          auditorOpinion\n          sourceDate\n          SREV\n          SPRE\n          RNII\n          RRGL\n          SIIB\n          SORE\n          RTLR\n          SCOR\n          SGRP\n          EFEX\n          EDOE\n          STIE\n          ENII\n          ELLP\n          SIAP\n          SLBA\n          EPAC\n          SSGA\n          ERAD\n          SDPR\n          SINN\n          SUIE\n          SOOE\n          ETOE\n          SOPI\n          SNIN\n          NGLA\n          NAFC\n          SNII\n          SNIE\n          SONT\n          EIBT\n          TTAX\n          TIAT\n          CMIN\n          CEIA\n          CGAP\n          NIBX\n          STXI\n          NINC\n          SANI\n          CIAC\n          XNIC\n          SDAJ\n          SDNI\n          SDWS\n          SDBF\n          DDPS1\n          VDES\n          __typename\n        }\n        balanceSheet {\n          source\n          updateType\n          statementDate\n          auditorName\n          auditorOpinion\n          sourceDate\n          ACSH\n          ACAE\n          ASTI\n          SCSI\n          AACR\n          ATRC\n          AITL\n          APPY\n          SOCA\n          ATCA\n          ACDB\n          SOEA\n          ANTL\n          APTC\n          ADEP\n          APPN\n          AGWI\n          AINT\n          SUPN\n          SINV\n          APRE\n          ALTR\n          SOLA\n          ADPA\n          SOAT\n          ATOT\n          LAPB\n          LPBA\n          LAEX\n          SPOL\n          LDBT\n          SOBL\n          LSTB\n          LSTD\n          LCLD\n          SOCL\n          LTCL\n          LLTD\n          LCLO\n          LTTD\n          STLD\n          SBDT\n          LMIN\n          SLTL\n          LTLL\n          SRPR\n          SPRS\n          SCMS\n          QPIC\n          QRED\n          QTSC\n          QEDG\n          QUGL\n          SOTE\n          QTLE\n          QTEL\n          QTCO\n          QTPO\n          STBP\n          __typename\n        }\n        cashFlowStatement {\n          source\n          periodLength\n          periodUnit\n          updateType\n          statementDate\n          auditorName\n          auditorOpinion\n          sourceDate\n          ONET\n          SDED\n          SAMT\n          OBDT\n          SNCI\n          OCRC\n          OCPD\n          SCTP\n          SCIP\n          SOCF\n          OTLO\n          SCEX\n          SICF\n          ITLI\n          SFCF\n          FCDP\n          FPSS\n          FPRD\n          FTLF\n          SFEE\n          SNCC\n          __typename\n        }\n        __typename\n      }\n      Interim {\n        periodEndDate\n        fiscalYear\n        periodType\n        periodLength\n        periodUnit\n        incomeStatement {\n          source\n          periodLength\n          periodUnit\n          updateType\n          statementDate\n          auditorName\n          auditorOpinion\n          sourceDate\n          SREV\n          SPRE\n          RNII\n          RRGL\n          SIIB\n          SORE\n          RTLR\n          SCOR\n          SGRP\n          EFEX\n          EDOE\n          STIE\n          ENII\n          ELLP\n          SIAP\n          SLBA\n          EPAC\n          SSGA\n          ERAD\n          SDPR\n          SINN\n          SUIE\n          SOOE\n          ETOE\n          SOPI\n          SNIN\n          NGLA\n          NAFC\n          SNII\n          SNIE\n          SONT\n          EIBT\n          TTAX\n          TIAT\n          CMIN\n          CEIA\n          CGAP\n          NIBX\n          STXI\n          NINC\n          SANI\n          CIAC\n          XNIC\n          SDAJ\n          SDNI\n          SDWS\n          SDBF\n          DDPS1\n          VDES\n          __typename\n        }\n        balanceSheet {\n          source\n          updateType\n          statementDate\n          auditorName\n          auditorOpinion\n          sourceDate\n          ACSH\n          ACAE\n          ASTI\n          SCSI\n          AACR\n          ATRC\n          AITL\n          APPY\n          SOCA\n          ATCA\n          ACDB\n          SOEA\n          ANTL\n          APTC\n          ADEP\n          APPN\n          AGWI\n          AINT\n          SUPN\n          SINV\n          APRE\n          ALTR\n          SOLA\n          ADPA\n          SOAT\n          ATOT\n          LAPB\n          LPBA\n          LAEX\n          SPOL\n          LDBT\n          SOBL\n          LSTB\n          LSTD\n          LCLD\n          SOCL\n          LTCL\n          LLTD\n          LCLO\n          LTTD\n          STLD\n          SBDT\n          LMIN\n          SLTL\n          LTLL\n          SRPR\n          SPRS\n          SCMS\n          QPIC\n          QRED\n          QTSC\n          QEDG\n          QUGL\n          SOTE\n          QTLE\n          QTEL\n          QTCO\n          QTPO\n          STBP\n          __typename\n        }\n        cashFlowStatement {\n          source\n          periodLength\n          periodUnit\n          updateType\n          statementDate\n          auditorName\n          auditorOpinion\n          sourceDate\n          ONET\n          SDED\n          SAMT\n          OBDT\n          SNCI\n          OCRC\n          OCPD\n          SCTP\n          SCIP\n          SOCF\n          OTLO\n          SCEX\n          SICF\n          ITLI\n          SFCF\n          FCDP\n          FPSS\n          FPRD\n          FTLF\n          SFEE\n          SNCC\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
        }
        return self.requester.post_request(payload)

    def get_market_cap(self, symbol):
        payload = {
            "operationName": "getMarketCap",
            "variables": {"symbol": symbol},
            "query": "query getMarketCap($symbol: String!) {\n  symbol(symbol: $symbol) {\n    id\n    metric {\n      id\n      atomMarketCap\n      __typename\n    }\n    __typename\n  }\n}\n",
        }
        return self.requester.post_request(payload)

    def get_many_events(self, symbol):
        payload = {
            "operationName": "getManyEvents",
            "variables": {"symbols": [symbol]},
            "query": "query getManyEvents($symbols: [String]!) {\n  manyEvents(symbols: $symbols) {\n    pastEvents {\n      EventId\n      name\n      eventType\n      startDate\n      transcriptId\n      LiveDialInStartDate\n      liveDialInPassword\n      liveDialInPhoneNumber\n      liveDialInStatus\n      transcriptDownloadStatus\n      actualSymbols\n      __typename\n    }\n    futureEvents {\n      EventId\n      name\n      eventType\n      startDate\n      transcriptId\n      LiveDialInStartDate\n      liveDialInPassword\n      liveDialInPhoneNumber\n      liveDialInStatus\n      actualSymbols\n      __typename\n    }\n    __typename\n  }\n}\n",
        }
        return self.requester.post_request(payload)

    def get_near_events(self, symbol):
        payload = {
            "operationName": "getNearEvents",
            "variables": {"symbols": [symbol]},
            "query": "query getNearEvents($symbols: [String]!) {\n  nearEvents(symbols: $symbols) {\n    pastEvents {\n      EventId\n      name\n      eventType\n      startDate\n      transcriptId\n      LiveDialInStartDate\n      liveDialInPassword\n      liveDialInPhoneNumber\n      liveDialInStatus\n      transcriptDownloadStatus\n      actualSymbols\n      __typename\n    }\n    futureEvents {\n      EventId\n      name\n      eventType\n      startDate\n      transcriptId\n      LiveDialInStartDate\n      liveDialInPassword\n      liveDialInPhoneNumber\n      liveDialInStatus\n      actualSymbols\n      __typename\n    }\n    __typename\n  }\n}\n",
        }
        return self.requester.post_request(payload)

    def get_news_feed(self, symbol):
        payload = {
            "operationName": "getNewsFeed",
            "variables": {
                "page": 0,
                "research": False,
            },
            "query": "query getNewsFeed($symbols: [String], $sectors: [String], $page: Int!, $overview: Boolean, $macro: Boolean, $research: Boolean, $enableResearch: Boolean, $includeBrokerageActions: Boolean, $onlyPlus: Boolean, $following: Boolean) {\n  newsFeed(symbols: $symbols, sectors: $sectors, page: $page, overview: $overview, macro: $macro, research: $research, enableResearch: $enableResearch, following: $following, includeBrokerageActions: $includeBrokerageActions, onlyPlus: $onlyPlus) {\n    news {\n      id\n      headlineText\n      revised\n      story\n      linkableCompanyRICs\n      linkableSectors\n      type\n      saved\n      inPlayBIPStory {\n        categories\n        __typename\n      }\n      isAtomPlus\n      __typename\n    }\n    page\n    hasMore\n    __typename\n  }\n}\n",
        }
        return self.requester.post_request(payload)

    def get_overview_data(self, symbol):
        payload = {
            "operationName": "getOverviewData",
            "variables": {"symbol": symbol},
            "query": "query getOverviewData($symbol: String!) {\n  symbol(symbol: $symbol) {\n    description\n    sector\n    industry\n    industryCode\n    marketCap\n    netDebt\n    ev\n    beta\n    borrowCost\n    nextEarningsDate\n    dividendPerShare\n    averageVolume\n    revenue\n    ebitda\n    ebit\n    eps\n    symbol\n    id\n    name\n    trRIC\n    trSearchAllCategory\n    metric {\n      id\n      atomMarketCap\n      price\n      __typename\n    }\n    ratiosData {\n      exchangeRate\n      reportingCurrency\n      sharesCount\n      __typename\n    }\n    currentFY\n    currentFQ\n    annualGuidance(startInclusive: 0, endExclusive: 2) {\n      id\n      period\n      periodYear\n      currency\n      adjEpsMax\n      adjEpsMin\n      gaapEpsMax\n      gaapEpsMin\n      adjEpsPriorMax\n      adjEpsPriorMin\n      gaapEpsPriorMax\n      gaapEpsPriorMin\n      adjRevenueMax\n      adjRevenueMin\n      gaapRevenueMax\n      gaapRevenueMin\n      adjRevenuePriorMax\n      adjRevenuePriorMin\n      gaapRevenuePriorMax\n      gaapRevenuePriorMin\n      __typename\n    }\n    sectorType\n    relativeConsensuses(startInclusive: 1, endExclusive: 2) {\n      id\n      fq\n      fy\n      isActual\n      dateHeld\n      datePeriodEnds\n      ...AllData\n      __typename\n    }\n    currentFY\n    currentFQ\n    ltmConsensuses(withFy0: true) {\n      id\n      fq\n      fy\n      isActual\n      dateHeld\n      datePeriodEnds\n      ...AllData\n      __typename\n    }\n    recommendationConsensuses {\n      NumberOfStrongBuy\n      NumberOfBuy\n      NumberOfHold\n      NumberOfSell\n      NumberOfStrongSell\n      __typename\n    }\n    topSector {\n      code\n      mnemonic\n      title\n      __typename\n    }\n    wiims {\n      id\n      benzingaId\n      created\n      updated\n      newsHeadline {\n        headlineText\n        revised\n        __typename\n      }\n      symbols {\n        symbol\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AllData on BetterConsensus {\n  REV\n  EBIT\n  Atom__EBITDA\n  EPS\n  TBVPS\n  BVPS\n  NAVPS\n  v1_NAV\n  SAL\n  GROSSINC\n  v1_DPS\n  FCFPS\n  NPROFITREP\n  CFPS\n  LLP\n  NIE\n  NET\n  CPS\n  NPA\n  ROA\n  RWA\n  BPS\n  NDT\n  v1_EPS\n  EBT\n  FFO\n  NAV\n  OPREXP\n  INTEXP\n  GRM\n  v1_ROA\n  GENADMEXP\n  CPX\n  EBITDAREP\n  v1_ROE\n  PRE\n  TOTDEBT\n  ROE\n  GPS\n  DPS\n  NII\n  TIER1\n  EBI\n  NETINVINC\n  EBITDA\n  Atom__NPROFIT\n  __typename\n}\n",
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
            "query": "query getPeriodGuidance($symbol: String!, $start: Int!, $end: Int!) {\n  symbol(symbol: $symbol) {\n    id\n    currentFY\n    currentFQ\n    annualGuidance(startInclusive: $start, endExclusive: $end) {\n      id\n      period\n      periodYear\n      currency\n      ...GuidanceData\n      __typename\n    }\n    quarterlyGuidance {\n      id\n      period\n      periodYear\n      currency\n      ...GuidanceData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment GuidanceData on Guidance {\n  adjEpsMax\n  adjEpsMin\n  gaapEpsMax\n  gaapEpsMin\n  adjEpsPriorMax\n  adjEpsPriorMin\n  gaapEpsPriorMax\n  gaapEpsPriorMin\n  adjRevenueMax\n  adjRevenueMin\n  gaapRevenueMax\n  gaapRevenueMin\n  adjRevenuePriorMax\n  adjRevenuePriorMin\n  gaapRevenuePriorMax\n  gaapRevenuePriorMin\n  __typename\n}\n",
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
            "query": "query getRelativeConsensuses($symbol: String!, $start: Int!, $end: Int!) {\n  symbol(symbol: $symbol) {\n    id\n    currentFY\n    currentFQ\n    relativeConsensuses(startInclusive: $start, endExclusive: $end) {\n      id\n      fq\n      fy\n      isActual\n      dateHeld\n      datePeriodEnds\n      ...AllData\n      __typename\n    }\n    next4Quarters {\n      id\n      fq\n      fy\n      isActual\n      dateHeld\n      datePeriodEnds\n      ...AllData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AllData on BetterConsensus {\n  REV\n  EBIT\n  Atom__EBITDA\n  EPS\n  TBVPS\n  BVPS\n  NAVPS\n  v1_NAV\n  SAL\n  GROSSINC\n  v1_DPS\n  FCFPS\n  NPROFITREP\n  CFPS\n  LLP\n  NIE\n  NET\n  CPS\n  NPA\n  ROA\n  RWA\n  BPS\n  NDT\n  v1_EPS\n  EBT\n  FFO\n  NAV\n  OPREXP\n  INTEXP\n  GRM\n  v1_ROA\n  GENADMEXP\n  CPX\n  EBITDAREP\n  v1_ROE\n  PRE\n  TOTDEBT\n  ROE\n  GPS\n  DPS\n  NII\n  TIER1\n  EBI\n  NETINVINC\n  EBITDA\n  Atom__NPROFIT\n  __typename\n}\n",
        }
        return self.requester.post_request(payload)

    def get_symbol(self, symbol):
        payload = {
            "operationName": "getSymbol",
            "variables": {"symbol": symbol},
            "query": "query getSymbol($symbol: String!) {\n  symbol(symbol: $symbol) {\n    id\n    symbol\n    name\n    description\n    CEO\n    exchange\n    iexSector\n    iexIndustry\n    sector\n    industry\n    industryCode\n    marketCap\n    netDebt\n    ev\n    beta\n    borrowCost\n    nextEarningsDate\n    dividendPerShare\n    averageVolume\n    revenue\n    ebitda\n    ebit\n    eps\n    listingStatus\n    trAssetCategory\n    trSearchAllCategory\n    metric {\n      id\n      atomMarketCap\n      price\n      __typename\n    }\n    kpiSnapshots {\n      id\n      sectorLabel\n      __typename\n    }\n    __typename\n  }\n}\n",
        }
        return self.requester.post_request(payload)
