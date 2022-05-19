from application import app, db
from flask import render_template, request, Response
import requests
from application.models import Characters

@app.route('/index', methods=['GET', 'POST'])
def index():
    name = requests.get('http://localhost:5001/name').text
    planet = requests.get('http://localhost:5002/planet').text
    databank = requests.post("http://localhost:5003/databank", data=planet).text
    return render_template('index.html', name=name, planet=planet, databank=databank)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host = '0.0.0.0')