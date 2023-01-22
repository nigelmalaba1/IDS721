from flask import Flask

app = Flask(__name__)

@app.route("/")

def breakfast():
    return "Your breakfast is eggs"

@app.route("/1")

def norepeat():

    return "Your breakfast is saussage"

@app.route("/tired")

def cafein():

    return "Your breakfast is coffee and bagel"

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
