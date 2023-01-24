from flask import Flask

app = Flask(__name__)

@app.route("/")

def breakfast():

 return "Your breakfast is eggs and croissants"   

@app.route("/dontrepeat")

def norepeat():

    return "Ok here is something new for you. Your breakfast is saussage, eggs and a bagel"

@app.route("/tired")

def caffein():

    return "Your breakfast is coffee and bagel because you're tired"

@app.route("/<dayoftheweek>")

def weekend(dayoftheweek):

    if(dayoftheweek == "Saturday"):
           return "You can eat anything you want today!"
    else:
        return "It's oatmeal today!"


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)