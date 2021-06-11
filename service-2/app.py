from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/get_coords', methods=['GET', 'POST'])
def coords():
    z = []
    x = random.randrange(-85, 85)
    z.append(x)
    y = random.randrange(-180, 180)
    z.append(y)
    return jsonify({'coordinates':z})

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)