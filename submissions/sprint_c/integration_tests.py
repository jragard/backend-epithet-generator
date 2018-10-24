import unittest
from flask_testing import TestCase
from app import app


class TestViews(TestCase):

    def create_app(self):
        self.app = app
        return self.app

    def test_generate_epithets(self):
        response = self.client.get('/')

        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json.keys(), ['epithet'])

    def test_vocabulary(self):
        response = self.client.get('/vocabulary')

        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json.keys(), ['vocabulary'])

    def test_quantity(self):
        response = self.client.get('/epithets/5')

        self.assert200(response)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json.keys(), ['quantity'])
        self.assertTrue(len(response.json['quantity']) == 5)

    def test_random(self):
        response_list = []

        for gets in range(1, 3):
            response = self.client.get('/random')
            self.assert200(response)
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.json.keys(), ['random'])
            response_list.append(response.json['random'])

        # Since this route serves a random number of epithets, this test may
        # occasionally fail, but it should be very rare
        self.assertFalse(len(response_list[0]) == len(response_list[1]))


if __name__ == '__main__':
    unittest.main()
