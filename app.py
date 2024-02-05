from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'API is running!'
    })

@app.route('/about')
def about():
    return jsonify({
        'message': 'About Page'
    })

if __name__ == '__main__':
    app.run(debug=True)
