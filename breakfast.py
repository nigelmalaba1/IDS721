from flask import Flask

app = Flask(__name__)

#create a list of breakfast items
breakfast = ["eggs", "croissants", "saussage", "bagel", "coffee", "oatmeal"]

# create a list of days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# create a list of fruits
fruits = ["apple", "banana", "orange", "grape", "strawberry", "blueberry", "raspberry"]

# create a list of beverages
beverages = ["coffee", "tea", "milk", "water", "juice"]

#If the user goes to the root path, return a string with 1 breakfast item,  1 day of the week, and 1 fruit, and 1 beverage
#If the user goes to the /dontrepeat path, return a string with 2 breakfast items
#If the user goes to the /tired path, return a string with 1 breakfast item and 1 beverage
#If the user goes to the /<dayoftheweek> path, return a string that says "You can eat anything you want today!" if it's Saturday, "Let's nourish up with some fruits before the start of the week" if it's Sunday, and "It's oatmeal today!" 

# create a route for the root path

@app.route("/")

#create a function that returns a string with 1 breakfast item,  1 day of the week, and 1 fruit, and 1 beverage

def breakfastfun():

    return " It's " + days[0] + ". Your breakfast is " + breakfast[0] + " and " + breakfast[1] + " with an" + fruits[0] + " and " + beverages[1] + "." 
  
#create a route for the /dontrepeat path
@app.route("/dontrepeat")

#create a function that returns a string with 2 breakfast items

def norepeat(): 
    return "Ok here is something new for you. Your breakfast is " + breakfast[2] + " and " + breakfast[3] + "."

#create a route for the /tired path
@app.route("/tired")

#create a function that returns a string with 1 breakfast item and 1 beverage
def caffein():
    return "Your breakfast is " + breakfast[4] + " and " + beverages[1] + " because you're tired"

#create a route for the /<dayoftheweek> path
@app.route("/<day>")

#create a function that returns a string that says "You can eat anything you want today!" if it's Saturday, "Let's nourish up with some fruits before the start of the week" if it's Sunday, and "It's oatmeal today!"
def weekend(day):
    #loop through the days of the week and print out the day of the week and the breakfast item for that day of the week
    if day == "Monday":
        return "It's " + days[0] + ". Your breakfast is " + breakfast[0] + "."
    if day == "Tuesday":
        return "It's " + days[1] + ". Your breakfast is " + breakfast[1] + "."
    if day == "Wednesday":
        return "It's " + days[2] + ". Your breakfast is " + breakfast[2] + "."
    if day == "Thursday":
        return "It's " + days[3] + ". Your breakfast is " + breakfast[3] + "."  
    if day == "Friday":
        return "It's " + days[4] + ". Your breakfast is " + breakfast[4] + "."
    if day == "Saturday":
        return "It's " + days[5] + ". Your breakfast is " + breakfast[5] + "."
    else:
        return "It's oatmeal today! You didn't specify what you want so I'm giving you oatmeal."

if __name__ == "__main__":
   # server = wsgiserver.WSGIServer(breakfast, port=5000, numthreads=2)
    #server.start()
    app.run(host='0.0.0.0', port=8080, debug=False)