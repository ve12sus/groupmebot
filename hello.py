from flask import Flask, request
import requests, json, re
import dial
 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        req_data = request.get_json()
        return dial.parse(req_data)
    return 'okay'

if __name__ == "__main__":
    app.run()
