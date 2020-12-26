from flask import Flask, render_template, request, url_for
import requests



app = Flask(__name__)

# startDateTime = "2017-08-01%2012:00:00"
# finishDateTime = "2017-08-04%2013:00:00"
# base_url = "https://staging1.alo-tech.com/api/?function=reportsCDRLogs&startdate={}&finishdate={}&"
# token = "app_token=ag9zfnRlbGVmb25pLXRlc3RyHwsSElRlbmFudEFwcGxpY2F0aW9ucxiAgICw46OcCQyiARVzdGFnaW5nMS5hbG8tdGVjaC5jb20"
# main_url = (base_url + token).format(startDateTime, finishDateTime )


# response = requests.get(main_url)

# json_data = response.json()["CallList"][1]
# x= [json_data[x] for x in json_data]


# https://staging1.alo-tech.com/api/?function=reportsCDRLogs&startdate=2017-08-01
# %2012:00:00&finishdate=2017-08-04%2013:00:00&app_token=ag9zfnRlbGVmb25pL
# XRlc3RyHwsSElRlbmFudEFwcGxpY2F0aW9ucxiAgICw46OcCQyiARVzdGFnaW5nMS5h
# bG8tdGVjaC5jb20

# response = requests.get(url + token)
# print(response)
# json_verisi = response.json()
# print(json_verisi["CallList"][0])
# # call_List = {
# #     "Calldate" : "A",
# #     "Called_num" : "B",
# #     "Callerid" : "C",
# #     "Answered" : "D",
# #     "Duration" : "E"
# }
@app.route("/calltable")
def callTable():
    return render_template("calltable.html")



@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        main_startDate = request.form.get("startDate")
        main_startTime = request.form.get("startTime").replace(":", "")
        startDate = "{}{}{}{}".format(main_startDate ,"%", main_startTime , ":00:00")
        main_finishDate = request.form.get("finishDate")
        main_finishTime = request.form.get("finishTime").replace(":", "")
        finishDate = "{}{}{}{}".format(main_finishDate ,"%", main_finishTime , ":00:00")
        return render_template("calltable.html", startDate = startDate, finishDate = finishDate )
    else:
        return render_template("calltable.html")


# @app.route("/toplam", methods = ["GET", "POST"])
# def toplam():
#     if request.method == "POST":
#         startDate = request.form.get("startdate")
#         startTime = request.form.get("startime")
        
#         return render_template("second.html" )
#     else:
#         return render_template("second.html")


if __name__ == "__main__":
    app.run(debug = True) 