from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name):
    return f'Hello {name}'


@app.route('/f/<value>')
def celsius_to_fahrenheit(value):
    fahrenheit = int(value)
    return f"{fahrenheit} fahrenheit is {fahrenheit * 9/5 + 32} celsius"


if __name__ == '__main__':
    app.run()
