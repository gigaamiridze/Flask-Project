from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register')
def register():
    return "This is register page" # TODO Generalize

if __name__ == '__main__':
    app.run(debug=True, port=7777)
