from sprint_b import app
from flask import jsonify
from helpers import EpithetGenerator


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
    epithets = EpithetGenerator.get_quantity_of_epithets(int(quantity))
    return jsonify({'quantity': epithets})


app.run()
