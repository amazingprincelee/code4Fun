from flask import Flask, jsonify


app = Flask(__name__)




@app.route('/in', methods=['GET'])
def home():
    return jsonify({"message":"Welcome to Flask server"})





if __name__ == "__main__":
    app.run(debug=True)