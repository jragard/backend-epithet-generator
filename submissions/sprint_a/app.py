from sprint_a import app
from flask import jsonify


@app.route('/')
def generate_epithets():
    return jsonify({'epithets': []})


@app.route('/vocabulary')
def vocabulary():
    return jsonify({'vocabulary': []})
