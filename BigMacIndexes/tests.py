import unittest
from django.test import Client


class ResponseTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_table(self):
        response = self.client.get('/table/')
        self.assertEqual(response.status_code, 200)

    def test_graph(self):
        response = self.client.get('/graph/')
        self.assertEqual(response.status_code, 200)

    def test_calculator(self):
        response = self.client.get('/calculator/')
        self.assertEqual(response.status_code, 200)
