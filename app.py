from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/goodbye/")
def goodbye_world():
    return "<p>Goodbye, World!</p>"

@app.route("/coder/")
def coder():
    return "<p>This web app was created in a class at Coder Academy.</p>"

# from flask import Flask
# from datetime import datetime

# app = Flask(__name__)

# # Your code here
# @app.route("/current_time/")
# def current_time():
#     return f"<p>{str(datetime.now().strftime('%H:%M'))}</p>"