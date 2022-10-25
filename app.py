from flask import Flask # import Flask library
import random


app = Flask(__name__) # set up app variable so that we can start writing routes

@app.route("/") # indicates the URL of the web page we'll need to visit in order to see our result. 
def homepage(): # defines the route function. Whatever this function returns will show up in the browser when you visit the URL.
    """Shows a greeting to the user.""" # doctring describing the route in a readable way
    return "Are you there, world? It\'s me, Ducky!" # returns the page contents

@app.route("/animal/<users_animal>")
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f"Wow, {users_animal}  is my favorite animal, too!"

@app.route("/dessert/<users_dessert>")
def favorite_dessert(users_dessert):
    """Display a message How did you know I liked {users_dessert}?"""
    return f"How did you know I liked, {users_dessert}?"

@app.route("/madlibs/<adjective>/<noun>")
def madlibs(adjective, noun):
    """A funny story"""
    return f"The panda saw a, {adjective} bird and thought it was a {noun}."

@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    """takes two numbers, multiplies them, and displays the results."""
    number_answer = int(number1) * int(number2)
    return f"{number1} times {number2} is {number_answer}"

@app.route("/sayntimes/<word>/<n>")
def say_n_times(word, n):
    display = True
    """repeat a string a given number of times"""
    if word.isalpha() and n.isdigit(): # checks if words are letters and n are numbers
        display = (word + " ") * int(n) + word
    else:
        word_response = "Invalid input. Please try again by entering a word and a number!"
    return display
    """ran pytest and got a valueError: invalid literal for int() with base 10:world
       test_app.py:: test_sayntimes_invalid - assert 500 == 200"""
    """tried to create a loop as per instructions of the assignment but got confused."""

@app.route("/dicegame")
def dicegame():
    """If the user rolls a 6, they win the game, otherwise, they lose."""
    dice = random.randint(1,6)
    results = ""
    if dice == 6:
        results = "You Won!"
    else:
        results = "You Lost!"
    return f"You rolled a {dice}. {results}"










if __name__ == "__main__":
    app.run(debug=True)