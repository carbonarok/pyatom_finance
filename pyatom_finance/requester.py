import json
import requests

from . import config as config
from .exceptions import AtomLoginError, StockCollectorRequesterError


class Requester:
    def __init__(self):
        pass

    def create_session(self):
        self.verify = True
        self.headers = {"Content-Type": "application/json"}

        self.session = requests.session()
        payload = {
            "username": config.SETTINGS.username,
            "password": config.SETTINGS.password,
        }
        resp = self.session.request(
            "POST",
            config.SETTINGS.atom_signin_url,
            data=json.dumps(payload),
            headers=self.headers,
        )
        if 199 < resp.status_code < 300:
            resp = resp.json()
            if not resp["success"]:
                raise AtomLoginError(
                    reason="Unable to login to Atom Finance", message=resp["error"]
                )
        else:
            raise StockCollectorRequesterError(
                reason="Bad HTTP statuss code", message=resp.text
            )

    def post_request(self, query):
        resp = self.session.request(
            "POST",
            config.SETTINGS.atom_url,
            data=json.dumps(query),
            headers=self.headers,
        )
        if 199 < resp.status_code < 300:
            return resp.json()
        else:
            raise StockCollectorRequesterError(
                reason="Bad HTTP status code", message=resp.text
            )
