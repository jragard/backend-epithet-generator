from __init__ import app
from flask import request, jsonify
from helpers import FileManager, Vocabulary, EpithetGenerator


@app.route('/')
def generate_epithets():
    single_epithet = EpithetGenerator.display_single_epithet()
    return jsonify({'epithets': single_epithet})


@app.route('/vocabulary')
def vocabulary():
    vocab_dataset = EpithetGenerator.display_vocab_dataset()
    return jsonify({'vocabulary': vocab_dataset})


@app.route('/epithets/<quantity>')
def quantity(quantity):
    epithets_quantity = EpithetGenerator.get_quantity_of_epithets(quantity)
    return jsonify({'quantity': epithets_quantity})


app.run()