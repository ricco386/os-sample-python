from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/ahoj")
def hello():
    return "Ahoj svet!"

if __name__ == "__main__":
    application.run()
