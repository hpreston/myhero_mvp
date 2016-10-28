#! /usr/bin/python
'''
    This is the Data Tier for a basic 3 tier application.
    The application was designed to provide a simple demo
    of a multi-tier application.

    As designed, all three tiers running on the same host,
    if running the app_server and data_servers on seperate
    hosts, update the varables appropriately.
'''
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
    tally = Counter()
    with open("votes.txt") as f:
        for line in f:
            line = line.rstrip()
            tally[line] += 1
    resp = make_response(jsonify(tally))
    return resp

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=int("5002"))

