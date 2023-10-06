from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def login_page():
    return render_template('cookie/cookie.html')


@app.route('/details', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        output = 'Hello!!!, Welcome ' + name + ''
        resp = make_response(output)
        resp.set_cookie('username', name)
        return resp

    resp = request.cookies.get('username', None)
    return resp


if __name__ == "__main__":
    app.run(debug=True)