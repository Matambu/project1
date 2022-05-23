from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)





@app.route('/index', methods=['GET', 'POST'])
def index():
    name = requests.get('http://localhost:5001/name').text
    planets = requests.get('http://localhost:5002/planet').text
    databank = requests.post("http://localhost:5003/databank")
    return render_template('index.html', name=name, planets=planets, databank=databank)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host = '0.0.0.0')