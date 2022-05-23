from flask import Flask, Response

import random


app = Flask(__name__)




@app.route('/name', methods=['GET'])
def name():
    names = ["Cal Kestis", "Kylo Ren", "Grand Inquisitor", "Ahsoka Tano", "Shaak-Ti", "Galen Marek", "Darth Bane", "Bail Organa", "R2-D2", "Obi-Wan Kenobi"]
    return Response(random.choices(names), mimetype='text/plain')

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)