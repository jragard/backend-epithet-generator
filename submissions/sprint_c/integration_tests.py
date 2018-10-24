import unittest
from flask_testing import TestCase
from app import app


class TestViews(TestCase):

    def create_app(self):
        self.app = app
        return self.app

    def test_generate_epithets(self):
        response = self.client.get('/vocabulary')
        print response
        self.assertEqual(str(response), '<TestResponse streamed [200 OK]>')


if __name__ == '__main__':
    unittest.main()
