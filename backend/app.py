from flask import Flask, render_template
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__,
            static_folder='../frontend/dist/static',
            template_folder='../frontend/dist')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1/message')
def message():
    return jsonify("This is a first message")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)