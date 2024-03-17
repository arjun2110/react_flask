# backend/app.py

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
