import argparse
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
import praw
import random

# Backend that gets picutres from reddit
# Chrome extension that makes requests to the backend

app = Flask(__name__)
Bootstrap(app)


def get_top_pics():
    r = praw.Reddit(user_agent="noprocrast by /u/godlikesme")
    submissions = r.get_subreddit('getmotivated').get_top_from_month(limit=20)
    pics = [submission.url for submission in submissions if "imgur" in submission.url]  # FIXME: not the best way to check for pics
    return pics


@app.route('/json')
def json_api():
    return jsonify(random_pic=random.choice(get_top_pics()))


@app.route('/')
def hello_world():
    # FIXME: accessing reddit api from http request is bad idea
    pics = get_top_pics()
    return render_template("index.html", pic_link=random.choice(pics))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Antiprocrastination app')
    parser.add_argument("port", metavar='port', type=int)
    args = parser.parse_args()

    app.run(port=args.port, debug=True)
