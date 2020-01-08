from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello!'

@app.route("/user/<name>")
def get_user_name(name):
    return "Hello {}".format(name)

if __name__ == '__main__':
    app.run()