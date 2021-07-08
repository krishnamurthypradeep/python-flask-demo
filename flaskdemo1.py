from flask import Flask

app = Flask(__name__)
# http://localhost:8080/
@app.route("/home")
def welcome():
    return "Relay Forward it works hdlkdlkdope"