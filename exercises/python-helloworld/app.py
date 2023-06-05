import json
from flask import Flask
from flask import json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

@app.route('/status')
def status():
    response = app.response_class(
        response =json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    return response
app.logger.info("hanno chiamato status")

@app.route('/metrics')
def status():
    response = app.response_class(
        response =json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    return response

app.logger.info("richiesta accettata")