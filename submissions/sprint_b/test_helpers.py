import unittest
import os
import shutil
from flask import json
from helpers import FileManager, Vocabulary, EpithetGenerator


class HelperTests(unittest.TestCase):

    path = './temp_dir/data.json'

    def setUp(self):
        data = {
            "Column1": "bar",
            "Column2": "foo",
            "Column3": "baz"
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
        self.assertEqual(FileManager.read_json(self.path), {
            "Column1": "bar",
            "Column2": "foo",
            "Column3": "baz"
        })
        self.assertEqual(type(FileManager.read_json(self.path)), dict)

    def test_from_file(self):
        self.assertEqual(Vocabulary.from_file(self.path), ({
            "Column1": "bar",
            "Column2": "foo",
            "Column3": "baz"
        }, ["Column1"]))

    def test_from_json(self):
        self.assertEqual(Vocabulary.from_json(self.path), ({
            "Column1": "bar",
            "Column2": "foo",
            "Column3": "baz"
        }, ["Column1"]))

    def test_strategies(self):
        self.assertEqual(Vocabulary.strategies('json'), Vocabulary.from_json)

    def test_get_single_epithet(self):
        data = Vocabulary.from_file('../../resources/data.json')
        data_keys = sorted(data[1])

        column1 = data[0][data_keys[0]]
        column2 = data[0][data_keys[1]]
        column3 = data[0][data_keys[2]]

        words = EpithetGenerator.get_single_epithet()[0]

        self.assertTrue(words[0] in column1)
        self.assertTrue(words[1] in column2)
        self.assertTrue(words[2] in column3)

    def test_display_single_epithet(self):
        full_epithet_data = EpithetGenerator.get_single_epithet()
        epithet_to_display = full_epithet_data[1]
        single_epithet_words = full_epithet_data[0]

        self.assertEqual(epithet_to_display, "Thou " + single_epithet_words[0] + ", " + single_epithet_words[1] + ", " + single_epithet_words[2] + "!")

    def test_get_quantity_of_epithets(self):
        quantity = 4
        epithet_list = EpithetGenerator.get_quantity_of_epithets(quantity)
        self.assertTrue(len(epithet_list) == quantity)

    # def test_display_vocab_dataset(self):
    #     data = Vocabulary.from_file(self.path)


# class SadHelperTests(unittest.TestCase):

#     path = './not_a_dir/data.json'

#     def test_get_extension(self):
#         self.assertEqual(FileManager.get_extension
#                          ('/Users/testDirectory/Ryan.json'),
#                          'csv')

#     def test_read_json(self):
#         self.assertEqual(FileManager.read_json(self.path), {"foo": "bar"})

#     def test_from_file(self):
#         self.assertEqual(Vocabulary.from_file(self.path), ({"foo": "bar"}, ["foo"]))

#     def test_from_json(self):
#         self.assertEqual(Vocabulary.from_json(self.path), ({"foo": "bar"}, ["foo"]))

#     def test_strategies(self):
#         self.assertEqual(Vocabulary.strategies('csv'), Vocabulary.from_json)


if __name__ == '__main__':
    unittest.main()
