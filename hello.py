from flask import Flask, request
import requests, json
import dial

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return 'Get'
    elif request.method == 'POST':
        resp = request.get_json(force=True)
        print resp
        return 'Post'

if __name__ == "__main__":
    app.run()
