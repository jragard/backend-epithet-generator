import os
import random
from flask import json


class FileManager:
    """Handle local file system IO"""

    @staticmethod
    def get_extension(path):
        """Get file extension from file path"""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources"""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]


class EpithetGenerator:

    @classmethod
    def get_single_epithet(cls):
        data = Vocabulary.from_file('../../resources/data.json')
        data_keys = sorted(data[1])

        word1 = random.choice(data[0][data_keys[0]])
        word2 = random.choice(data[0][data_keys[1]])
        word3 = random.choice(data[0][data_keys[2]])

        return ([word1, word2, word3], "Thou " + word1 + ", " + word2 + ", " + word3 + "!")

    @classmethod
    def display_single_epithet(cls):
        epithet_to_display = cls.get_single_epithet()[1]
        return epithet_to_display

    @classmethod
    def get_quantity_of_epithets(cls, quantity):
        counter = 0
        epithet_list = []
        while counter < quantity:
            epithet = cls.display_single_epithet()
            epithet_list.append(epithet)
            counter += 1

        return epithet_list

    @classmethod
    def display_vocab_dataset(cls):
        data = Vocabulary.from_file('../../resources/data.json')[0]
        column1_list = data["Column 1"]
        column2_list = data["Column 2"]
        column3_list = data["Column 3"] 

        return (column1_list, column2_list, column3_list)

# EpithetGenerator.display_vocab_dataset()