from unittest import TestCase

from pyatom_finance import Requester
from pyatom_finance import config


class TestCollector(TestCase):
    def setUp(self):
        config.load()
        self.requester = Requester()

    def test_create_session(self):
        self.requester.create_session()
