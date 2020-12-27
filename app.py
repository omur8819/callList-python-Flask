from flask import Flask, render_template, request, url_for, redirect
import requests, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods = ["GET", "POST"])
def api():
    if request.method == "POST":

     # get dates from index html
        startdate = request.form.get("startDate").replace(" ", "%")
        finishdate = request.form.get("finishDate").replace(" ", "%")

        # # get json data from api
        url = "https://staging1.alo-tech.com/api/?function=reportsCDRLogs&startdate={}&finishdate={}"
        end_point = url.format(startdate, finishdate)
        app_token = "ag9zfnRlbGVmb25pLXRlc3RyHwsSElRlbmFudEFwcGxpY2F0aW9ucxiAgICw46OcCQyiARVzdGFnaW5nMS5hbG8tdGVjaC5jb20"
        data = requests.get(end_point, params={"app_token": app_token})
        json_data = data.json()["CallList"]

        return render_template("calltable.html", callData =json_data )
    else:
        return render_template("calltable.html")

@app.route("/calltable")
def callTable():
    return render_template("calltable.html")
if __name__ == "__main__":
    app.run(debug = True) 