from flask import Flask, Response, request
import random
from application import app

@app.route('/planet', methods=['GET'])
def planet():
    planets = ["Tatooine", "Coruscant", "Kamino", "Ryloth", "Shili", "Kashyyyk"]
    return Response(random.choices(planets), mimetype="text/plain")