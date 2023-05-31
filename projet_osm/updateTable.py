from flask import Flask, jsonify

app = Flask(__name__)

# Dicionario de exemplo
data = {1: ['jose', 2], 2: ['ana', 3]}

@app.route('/_data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
