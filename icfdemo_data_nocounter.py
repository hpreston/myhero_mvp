__author__ = 'hapresto'

from flask import Flask, make_response, request, jsonify
import datetime
from collections import Counter

app = Flask(__name__)

@app.route("/hero_list")
def hero_list():
    hero_list = []
    with open("heros.txt") as f:
        for line in f:
            line = line.rstrip()
            hero_list.append(line)
    resp = make_response(jsonify(heros=hero_list))
    return resp

@app.route("/vote/<hero>")
def vote(hero):
    with open("votes.txt", "a") as f:
        f.write(hero + "\n")
    resp = make_response(jsonify(result="1"))
    return resp

@app.route("/results")
def results():
    votes = []
    with open("votes.txt") as f:
        for line in f:
            line = line.rstrip()
            votes.append(line)
    heros = set(votes)
    tally = {};
    for hero in heros:
        tally[hero] = 0
    for vote in votes:
        tally[vote] += 1
    resp = make_response(jsonify(tally))
    return resp


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=int("5002"))
