# Explore the ‘Flask’ module and create a web server using Flask & Python.

# pip install flask
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# To run the flask application
# flask --app filename run
