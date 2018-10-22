import unittest
import os
import shutil
from flask import json
from helpers import FileManager, Vocabulary


class HelperTests(unittest.TestCase):

    path = './temp_dir/data.json'

    def setUp(self):
        data = {
            "foo": "bar"
        }

        if os.path.isdir('temp_dir'):
            shutil.rmtree('temp_dir')
            os.mkdir('./temp_dir')
            with open(self.path, 'w') as test_file:
                json.dump(data, test_file)
        else:
            os.mkdir('./temp_dir')
            with open(self.path, 'w') as test_file:
                json.dump(data, test_file)
        
    def tearDown(self):
        shutil.rmtree('./temp_dir')

    def test_get_extension(self):
        self.assertEqual(FileManager.get_extension
                         ('/Users/testDirectory/Ryan.json'),
                         'json')

    def test_read_json(self):
        self.assertEqual(FileManager.read_json(self.path), {"foo": "bar"})
        self.assertEqual(type(FileManager.read_json(self.path)), dict)

    def test_from_file(self):
        self.assertEqual(Vocabulary.from_file(self.path), ({"foo": "bar"}, ["foo"]))

    def test_from_json(self):
        self.assertEqual(Vocabulary.from_json(self.path), ({"foo": "bar"}, ["foo"]))

    def test_strategies(self):
        self.assertEqual(Vocabulary.strategies('json'), Vocabulary.from_json)


if __name__ == '__main__':
    unittest.main()
