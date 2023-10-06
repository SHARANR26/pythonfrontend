from flask import Flask
app = Flask(__name__)


@app.route("/name")
def index():
    return "Homepage of NewApp"


if __name__ == "__main__":
    app.run(debug=True)
