from flask import Flask, Response, request
import requests

app = Flask(__name__)







if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)

@app.route('/databank', methods=['POST'])
def databank():
    planet = request.data.decode('utf-8')
    if planet == "Tatooine":
        databank = "Home of Skywalker"
    elif planet == "Coruscant":
        databank = "Home of The Senate"
    elif planet == "Kamino":
        databank = "Home of The Clones"
    elif planet == "Ryloth":
        databank = "Home of The Twilek"
    elif planet == "Shili":
        databank = "Home of Ahsoka Tano & Shaak-Ti"
    elif planet == "Kashyyyk":
        databank = "Home of The Wookies"
    else:
        databank = "No databank entry"
    return Response(databank, mimetype="text/plain")
    
    