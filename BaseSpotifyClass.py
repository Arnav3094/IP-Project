import requests
import base64
import datetime as dt
from urllib.parse import urlencode
from pprint import pprint as pp
import pandas as pd
from pandas import DataFrame as DF
from pandas import Series as S
import numpy as np
import json
import time


def get_token_data():
    return {'grant_type': 'client_credentials'}


class SpotifyAPI:
    access_token = None
    access_token_expires = None
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = 'https://accounts.spotify.com/api/token'
        self.client_creds = None
        self.access_token_did_expire = None

    def get_client_creds(self):
        """
        Returns base64 encoded client_creds
        """
        assert self.client_secret, self.client_id is not None
        self.client_creds = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        return self.client_creds

    def get_token_headers(self):
        client_creds_b64 = self.get_client_creds()
        return {'Authorization': f'Basic {client_creds_b64}'}

    def auth(self):
        """
        Performs authorization
        returns True if access granted, else False
        sets the access_token details for the object
        """
        r = requests.post(self.token_url, data=get_token_data(), headers=self.get_token_headers())
        if r.status_code not in range(200, 299):
            print(f"Something went wrong.\n[Status Code] {r.status_code}")
            return False
        data = r.json()
        now = dt.datetime.now()
        self.access_token = data['access_token']
        expires_in = data['expires_in']
        self.access_token_expires = now + dt.timedelta(seconds=expires_in)
        self.access_token_did_expire = self.access_token_expires <= now
        return self.access_token
