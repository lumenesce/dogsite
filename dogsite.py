#!/bin/python3
# ?? not sure what that is ^

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_img():
    url = "https://dog.ceo/api/breeds/image/random"
    response = json.loads(requests.request("GET", url).text)    # {json has keys 'message' and 'status'}
    dog_img = response["message"]
    return dog_img


@app.route("/")
def index():
    dog_img = get_img()
    return render_template("index.html", dog_img=dog_img)

app.run(host="0.0.0.0", port=80, debug=True)