from flask import Flask, request
import requests, json, re
 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def hello():
    if request.method == 'GET':
        return "Hello World from flask"
    elif request.method == 'POST':
        data = request.get_json()
        content = data['text']
        if re.match(r'/ links', content):
            payload = {"bot_id": "f9b366898c181f1f3ef76da9f6", "text": "Here's the last 3 links:"}
            r = requests.post("https://api.groupme.com/v3/bots/post", data=payload)
            return 'hello world from post'
        else:
            return 'done'

if __name__ == "__main__":
    app.run()
