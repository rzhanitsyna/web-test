import os
import json
import requests
import unittest
from objects import *

REST_URL = 'https://restfulapi.ru/api/v2'


class AuthTest(unittest.TestCase):
    def test_successful(self):
        r = requests.post(REST_URL + '/auth/FSPO', data=json.dumps({
            "serviceLogin": os.environ["LOGIN"],
            "servicePassword": os.environ["PASS"]
        }))
        resp = r.json()
        resp: Response[User] = Response.parse_obj(resp)
        assert resp.error is None
        assert resp.result is not None

    def test_wrong(self):
        r = requests.post(REST_URL + '/auth/FSPO', data=json.dumps({
            "serviceLogin": "1",
            "servicePassword": "2"
        }))
        resp = r.json()
        resp: Response[User] = Response.parse_obj(resp)
        assert resp.error.message == 'Неверный логин или пароль'


class UniversityTest(unittest.TestCase):
    def test_list(self):
        r = requests.get(REST_URL + '/universities')
        resp = r.json()
        resp: Response[User] = Response.parse_obj(resp)
        assert resp.error is None


class GroupTest(unittest.TestCase):
    def test_list(self):
        r = requests.get(REST_URL + '/universities/FSPO/groups')
        resp = r.json()
        resp: Response[User] = Response.parse_obj(resp)
        assert resp.error is None


if __name__ == '__main__':
    unittest.main()
