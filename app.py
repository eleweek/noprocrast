import argparse
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Antiprocrastination app')
    parser.add_argument("port", metavar='port', type=int)
    args = parser.parse_args()

    app.run(port=args.port, debug=True)
