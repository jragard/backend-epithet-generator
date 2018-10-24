import unittest
from flask_testing import TestCase, Twill
from flask import jsonify
from app import app
from helpers import EpithetGenerator


class TestViews(TestCase):

    def create_app(self):
        self.app = app
        return self.app

    def test_generate_epithets(self):
        response = self.client.get('/')
        self.assertEqual(str(response), '<TestResponse streamed [200 OK]>')

    def test_something_with_twill(self):
        with Twill(self.app, port=3000) as t:
            t.browser.go(t.url("/"))

    def test_vocabulary(self):
        response = self.client.get('/vocabulary')
        # vocab_dataset = EpithetGenerator.display_vocab_dataset()
        self.assertEqual(str(response), '<TestResponse streamed [200 OK]>')
        # self.assertEqual(response.json, jsonify(vocab_dataset))

    def test_quantity(self):
        response = self.client.get('/epithets/5')
        self.assertEqual(str(response), '<TestResponse streamed [200 OK]>')

    def test_random(self):
        response = self.client.get('/random')
        self.assertEqual(str(response), '<TestResponse streamed [200 OK]>')


if __name__ == '__main__':
    unittest.main()
