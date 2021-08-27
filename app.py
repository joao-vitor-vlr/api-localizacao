from flask import Flask, redirect, url_for, render_template, request, jsonify
from geopy import Nominatim, distance
import time
import pandas as pd
from pprint import pprint


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("geo.html")
    

@app.route("/local", methods=["POST"])
def location():
    req = request.json["local"]

    apps = Nominatim(user_agent="tutorial")
    # get location raw data
    location = apps.geocode(req).raw
    # print raw data
    return jsonify(location)

@app.route("/local/distance", methods=["POST"])
def distancia():
    req1 = (request.json["local_Start"])
    req2 = (request.json["local_End"])

    apps = Nominatim(user_agent="tutorial")
    # get location raw data
    location_Start = apps.geocode(req1)
    location_End = apps.geocode(req2)

    
    distancia = distance.distance((location_Start['lat'], location_Start['lon']), (location_End['lat'], location_End['lon'])).km
    # print raw data
    return jsonify(distancia)





