from application import app
from flask import Flask, request, Response
import random

@app.route('/name', methods=['GET'])
def name():
    names = ["Cal Kestis", "Kylo Ren", "Grand Inquisitor", "Ahsoka Tano", "Shaak-Ti", "Galen Marek", "Darth Bane", "Bail Organa", "R2-D2", "Obi-Wan Kenobi"]
    return Response(random.choices(names), mimetype='text/plain')