__author__ = 'hapresto'

from flask import Flask, make_response, request, jsonify
import datetime
import urllib
import json

app = Flask(__name__)

data_server = "http://127.0.0.1:5002"


@app.route("/hero_list")
def hero_list():
    u = urllib.urlopen(data_server + "/hero_list")
    page = u.read()
    hero_list = json.loads(page)["heros"]

    resp = make_response(jsonify(heros=hero_list))
    return resp

@app.route("/vote/<hero>")
def vote(hero):
    u = urllib.urlopen(data_server + "/vote/" + hero)
    page = u.read()
    result = json.loads(page)['result']
    if (result == "1"):
        resp = make_response(jsonify(result="vote accepted"))
    else:
        resp = make_response(jsonify(result="vote rejected"))
    return resp

@app.route("/results")
def results():
    u = urllib.urlopen(data_server + "/results")
    page = u.read()
    tally = json.loads(page)

    resp = make_response(jsonify(tally))
    return resp


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=int("5001"))

