from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "WELCOME TO THE PAGE"

@app.route("/index")
def index():
    return "WELCOME TO THE INDEX PAGE"

@app.route("/about")
def about():
    return "Yeh Pannu ka about page hai!"



if __name__ == '__main__':
    app.run(debug=True)