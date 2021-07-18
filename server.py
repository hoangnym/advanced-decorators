from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://i.giphy.com/3o7aCSPqXE5C6T8tBC.gif'>"

@app.route('/<int:number>')
def guess(number):
    if number > random_number:
        return "<h1 style='color:red;'>Too low, try again!</h1>" \
               "<img src='https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp'>"
    elif number < random_number:
        return "<h1 style='color:purple;'>Too high, try again!</h1>" \
               "<img src='https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp'>"
    else:
        return "<h1 style='color:green;'>You found me!</h1>" \
               "<img src='https://i.giphy.com/media/4T7e4DmcrP9du/giphy.webp'>"

if __name__ == '__main__':
    app.run(debug=True)