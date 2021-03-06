from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/get_date', methods=['GET', 'POST'])
def Date():
    date = random.randrange(-3000, 2021)
    return jsonify(date)

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)