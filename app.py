from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return f'Hello {name}'

@app.route('/f')
@app.route('/f/<celsius>')
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"{celsius} Celsius degree is {fahrenheit} Fahrenheit degree."



if __name__ == '__main__':
    app.run()
