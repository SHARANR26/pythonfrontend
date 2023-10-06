from flask import *
import datetime
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["name"])
        print(request.form["email"])
        utc_dt = datetime.datetime.utcnow()

        return render_template("welcome.html", name=request.form["name"],email =request.form["email"],
                               utc_dt=datetime.datetime.utcnow())

    return render_template("http_method_form.html")


if __name__ == "__main__":
    app.run(debug=True)