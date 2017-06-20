from flask import Flask, request
import requests, json, re
import dial
 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "Hello World from flask"
    elif request.method == 'POST':
        data = request.get_json()
        content = data['text']
        if re.match(r'/ links', content):
            dial.paging(3)
        else:
            return 'done'

if __name__ == "__main__":
    app.run()
