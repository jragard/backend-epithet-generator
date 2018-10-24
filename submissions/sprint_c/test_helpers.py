import unittest
import os
import shutil
from flask import json
from helpers import FileManager, Vocabulary, EpithetGenerator


class HelperTests(unittest.TestCase):

    path = './temp_dir/data.json'
    sad_path = './fake_dir/data.csv'

    def setUp(self):
        data = {
            "Column1": "bar",
            "Column2": "foo",
            "Column3": "baz"
        }

        if os.path.isdir('temp_dir'):
            shutil.rmtree('temp_dir')
            os.mkdir('./temp_dir')
            with open('./temp_dir/data.json', 'w') as test_file:
                json.dump(data, test_file)
        else:
            os.mkdir('./temp_dir')
            with open('./temp_dir/data.json', 'w') as test_file:
                json.dump(data, test_file)

    def tearDown(self):
        shutil.rmtree('./temp_dir')

    def test_get_extension(self):
        self.assertEqual(FileManager.get_extension(self.path), 'json')

    def test_sad_path_get_extension(self):
        try:
            self.assertEqual(FileManager.get_extension(self.sad_path), 'json')
        except Exception as ex:
            self.assertEqual(type(ex), AssertionError)

    def test_read_json(self):
        self.assertEqual(FileManager.read_json(self.path), {
            "Column1": "bar",
            "Column2": "foo",
            "Column3": "baz"
        })

    def test_sad_read_json(self):
        try:
            self.assertEqual(FileManager.read_json(self.sad_path), {
                "Column1": "bar",
                "Column2": "foo",
                "Column3": "baz"
            })
        except Exception as ex:
            self.assertEqual(type(ex), IOError)

    def test_read_json_type(self):
        self.assertEqual(type(FileManager.read_json(self.path)), dict)

    def test_sad_read_json_type(self):
        try:
            self.assertEqual(type(FileManager.read_json(self.sad_path)), dict)
        except Exception as ex:
            self.assertEqual(type(ex), IOError)

    def test_from_file(self):
        self.assertEqual(Vocabulary.from_file(self.path), ({
            "Column1": "bar",
            "Column2": "foo",
            "Column3": "baz"
        }, ["Column1", "Column3", "Column2"]))

    def test_sad_from_file(self):
        try:
            self.assertEqual(Vocabulary.from_file(self.sad_path), ({
                "Column1": "bar",
                "Column2": "foo",
                "Column3": "baz"
            }, ["Column1", "Column3", "Column2"]))
        except Exception as ex:
            self.assertEqual(type(ex), KeyError)

    def test_from_json(self):
        self.assertEqual(Vocabulary.from_json(self.path), ({
            "Column1": "bar",
            "Column2": "foo",
            "Column3": "baz"
        }, ["Column1", "Column3", "Column2"]))

    def test_sad_from_json(self):
        try:
            self.assertEqual(Vocabulary.from_json(self.sad_path), ({
                "Column1": "bar",
                "Column2": "foo",
                "Column3": "baz"
            }, ["Column1", "Column3", "Column2"]))
        except Exception as ex:
            self.assertEqual(type(ex), IOError)

    def test_strategies(self):
        self.assertEqual(Vocabulary.strategies('json'), Vocabulary.from_json)

    def test_sad_strategies(self):
        try:
            self.assertEqual(Vocabulary.strategies('csv') ==
                             Vocabulary.from_json)
        except Exception as ex:
            self.assertEqual(type(ex), KeyError)

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

    def test_sad_get_single_epithet(self):
        try:
            data = Vocabulary.from_file(self.sad_path)
            data_keys = sorted(data[1])

            column1 = data[0][data_keys[0]]
            column2 = data[0][data_keys[1]]
            column3 = data[0][data_keys[2]]

            words = EpithetGenerator.get_single_epithet()[0]

            self.assertTrue(words[0] in column1)
            self.assertTrue(words[1] in column2)
            self.assertTrue(words[2] in column3)
        except Exception as ex:
            self.assertEqual(type(ex), KeyError)

    def test_display_single_epithet(self):
        full_epithet_data = EpithetGenerator.get_single_epithet()
        epithet_to_display = full_epithet_data[1]
        single_epithet = full_epithet_data[0]

        self.assertEqual(epithet_to_display, "Thou " +
                         single_epithet[0] + ", " + single_epithet[1] +
                         ", " + single_epithet[2] + "!")

    def test_sad_display_single_epithet(self):
        full_epithet_data = EpithetGenerator.get_single_epithet()
        epithet_to_display = full_epithet_data[1]
        single_epithet = full_epithet_data[0]

        try:
            self.assertEqual(epithet_to_display, "Thou " +
                             single_epithet[1] + ", " + single_epithet[2] +
                             ", " + single_epithet[0] + "!")
        except Exception as ex:
            self.assertEqual(type(ex), AssertionError)

    def test_get_quantity_of_epithets(self):
        quantity = 4
        epithet_list = EpithetGenerator.get_quantity_of_epithets(quantity)
        self.assertTrue(len(epithet_list) == quantity)

    def test_sad_get_quantity_of_epithets(self):
        try:
            quantity = 4
            epithet_list = EpithetGenerator.get_quantity_of_epithets(quantity)
            self.assertTrue(len(epithet_list) != quantity)
        except Exception as ex:
            self.assertEqual(type(ex), AssertionError)

    def test_display_vocab_dataset(self):
        data_test = Vocabulary.from_file(self.path)
        self.assertEqual(data_test, ({
            "Column1": "bar",
            "Column3": "baz",
            "Column2": "foo"
            }, ["Column1", "Column3", "Column2"]))

    def test_sad_display_vocab_dataset(self):
        try:
            data_test = Vocabulary.from_file(self.sad_path)
            self.assertEqual(data_test, ({
                "Column1": "bar",
                "Column3": "baz",
                "Column2": "foo"
                }, ["Column1", "Column3", "Column2"]))
        except Exception as ex:
            self.assertEqual(type(ex), KeyError)


if __name__ == '__main__':
    unittest.main()
