from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_date', methods=['GET'])
def date():
    date = str(random.randrange(-2000, 2000))
    return date

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)