from flask import Flask, request
import requests
 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "Hello World from flask"
    else:
	payload = {"bot_id": "f9b366898c181f1f3ef76da9f6", "text": "Hello world"}
	r = requests.post("https://api.groupme.com/v3/bots/post", data=payload)


if __name__ == "__main__":
    app.run()
