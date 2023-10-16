import unittest
import sb_requests.simple_books_req as sbr

class TestBooks(unittest.TestCase):
    def test_get_status(self):
        resp = sbr.get_status()
        assert isinstance(resp, str)
        #print(type(resp))


    def test_submit_order(self):
        resp = sbr.submit_order()
        created = bool(resp["created"])
        assert created
        print(resp)
