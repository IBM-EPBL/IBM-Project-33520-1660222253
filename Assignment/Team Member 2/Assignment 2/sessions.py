from flask import *
app = Flask(__name__)


@app.route('/')
def setcookie():
    res = make_response("Cookie is set")
    res.set_cookie("device", "Dell")
    res.set_cookie("name", "Shaju")
    return res


if __name__ == "__main__":
    app.run(debug = True)
    