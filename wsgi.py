from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "OpenShift Hello KPST World!"

if __name__ == "__main__":
    application.run()
