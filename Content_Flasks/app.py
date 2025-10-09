# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/goodbye/")
# def goodbye_world():
#     return "<p>Goodbye, World!</p>"

# @app.route("/coder/")
# def coder():
#     return "<p>This web app was created in a class at Coder Academy.</p>"



# from flask import Flask
# from datetime import datetime

# app = Flask(__name__)

# # Your code here
# @app.route("/current_time/")
# def current_time():
#     return f"<p>{str(datetime.now().strftime('%H:%M'))}</p>"


# from flask import Flask
# import json
# from datetime import datetime

# app = Flask(__name__)

# @app.route("/")
# def homepage():
#     return """<p>Hi, welcome to my API! Here are the endpoints that are available:</p>
#     <ul>
#     <li>Current Time: /time</li>
#     <li>Educator Info: /educators</li>
#     </ul>"""

# @app.route("/time")
# def current_time():
#     time_dict = {"current time": str(datetime.now().strftime('%H:%M'))}
#     return json.dumps(time_dict)

# @app.route("/educators")
# def educators():
#     educator_dict = {
#         "educators": [
#             {
#                 "Name": "Oliver",
#                 "Specialty": "Automated testing"
#             },
#             {
#                 "Name": "Jairo",
#                 "Specialty": "Discrete Mathematics"
#             },
#             {
#                 "Name": "Amir",
#                 "Specialty": "Web Development"
#             },
#             {
#                 "Name": "Iryna",
#                 "Specialty": "Database Engineering"
#             },
#             {
#                 "Name": "George",
#                 "Specialty": "Internet Security"
#             },
#         ]
#     }
#     return json.dumps(educator_dict)





# import random
# import json
# from flask import Flask, Response

# app = Flask(__name__)

# # Your code here
# @app.route("/coinflip")
# def coin_flip():
#     """"Coin flip function"""
#     outcomes = ["Heads", "Tails"]
#     choice = random.choice(outcomes)
#     result_json = json.dumps({"result": choice})
#     return Response(result_json, content_type="application/json")

# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask

# app = Flask(__name__)

# @app.route("/<some_value>")
# def some_page(some_value):
#     return f"<p>You gave the value {some_value} in the route!</p>"


from flask import Flask, abort
import json

app = Flask(__name__)

@app.route("/calculator/<int:first_number>/add/<int:second_number>")
def add(first_number, second_number):
    output = {
        "operation": f"{first_number} plus {second_number}",
        "result": first_number+second_number
    }
    return json.dumps(output)

@app.route("/calculator/<int:first_number>/subtract/<int:second_number>")
def subtract(first_number, second_number):
    output = {
        "operation": f"{first_number} minus {second_number}",
        "result": first_number-second_number
    }
    return json.dumps(output)

@app.route("/calculator/<int:first_number>/multiply/<int:second_number>")
def multiply(first_number, second_number):
    output = {
        "operation": f"{first_number} multiplied by {second_number}",
        "result": first_number*second_number
    }
    return json.dumps(output)

@app.route("/calculator/<int:first_number>/divide/<int:second_number>")
def divide(first_number, second_number):
    output = {
        "operation": f"{first_number} divided by {second_number}",
        "result": first_number/second_number
    }
    return json.dumps(output)
