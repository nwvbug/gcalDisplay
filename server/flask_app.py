from flask import Flask
from main import *
from flask_cors import CORS, cross_origin
app = Flask(__name__)


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin: *'

print("Server's starting, we potentially poggin")
startServer()

homefile = open("webpage/index.html", "r")
home = homefile.read()
homefile.close()

@app.route("/")
def mainSite():
    return home


@app.route("/notify", methods=['POST', 'GET'])
@cross_origin()
def notify():
    notificationData = request.json

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)