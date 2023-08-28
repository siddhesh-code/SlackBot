from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/')
def index():
    return "Hello, this is my SlackBot server!"

if __name__ == '__main__':
    app.run(port=5000)
