#!/bin/python3
# ?? not sure what that is ^

from flask import Flask, render_template
import requests
import json

application = Flask(__name__)

def get_img():
    url = "https://dog.ceo/api/breeds/image/random"
    response = json.loads(requests.request("GET", url).text)    # {json has keys 'message' and 'status'}
    dog_img = response["message"]
    return dog_img


@application.route("/")
def index():
    dog_img = get_img()
    return render_template("index.html", dog_img=dog_img)

if __name__ == '__main__':
    # for elastic beanstalk
    application.run()

    # for local debugging
    # application.run(host="0.0.0.0", port=80, debug=True)