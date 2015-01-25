'''
    This is the Web Tier for a basic 3 tier application.
    The application was designed to provide a simple demo
    for Cisco Intercloud Fabric.

    As designed, all three tiers running on the same host,
    if running the app_server and data_servers on seperate
    hosts, update the varables appropriately.
'''

from flask import Flask, render_template, request, jsonify
import datetime
import urllib
import json


app = Flask(__name__)

app_server = "http://127.0.0.1:5001"

@app.route("/")
def template_test():
    # Check for submitted vote
    vote = request.args.get('hero')
    if (vote):
        v = urllib.urlopen(app_server + "/vote/" + vote)

    u = urllib.urlopen(app_server + "/hero_list")
    page = u.read()
    hero_list = json.loads(page)["heros"]
    return render_template('home.html', hero_list=hero_list, title="Intercloud Fabric Demo Applicaiton", current_time=datetime.datetime.now())

@app.route("/about")
def about():
    return render_template('about.html', title="About", current_time=datetime.datetime.now())

@app.route("/results")
def results():
    u = urllib.urlopen(app_server + "/results")
    page = u.read()
    tally = json.loads(page)
    tally = sorted(tally.items(), key = lambda (k,v): v, reverse=True)
    return render_template('results.html', tally = tally, title="Results", current_time=datetime.datetime.now())

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')



