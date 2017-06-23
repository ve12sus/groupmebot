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
            name = dial.captureName(content)
            if name:
                dial.paging(3, name)
            else:
                dial.paging(3)
        elif re.match(r'/ likes', content):
            name = dial.captureName(content)
            if name:
                dial.getLikes(3, name)
            else:
                dial.botPost('Nobody by that name is in this group.')
        else:
            return 'done'

if __name__ == "__main__":
    app.run()
