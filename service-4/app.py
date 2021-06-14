from flask import Flask, request

app = Flask(__name__)

@app.route('/get_hint', methods=['GET', 'POST'])
def Hint():
    coordinates = request.get_json()
    if coordinates['x'] > 85:
        hint = "Orbit"
        return hint
    elif coordinates['x'] > 72:
        hint = "The Arctic"
        return hint
    elif coordinates['x'] < -60:
        hint = "Antarctica"
        return hint
    elif coordinates['x'] > 34 and coordinates['y'] > -33 and coordinates['y'] < 46:
        hint = "Europe"
        return hint
    elif coordinates['x'] < 35 and coordinates['y'] > -33 and coordinates['y'] < 61:
        hint = "Africa & Middle East"
        return hint
    elif coordinates['y'] < -32:
        hint = "The Americas"
        return hint
    else:
        hint = "Asia & Oceania"
        return hint

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)