from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_coords', methods=['GET'])
def coords():
    x = str(random.randrange(-85, 85))
    y = str(random.randrange(-180, 180))
    return x + ", " + y

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)