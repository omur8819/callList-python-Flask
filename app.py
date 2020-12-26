from flask import Flask, render_template, request, url_for
import requests



app = Flask(__name__)

# https://staging1.alo-tech.com/api/?function=reportsCDRLogs&startdate=2017-08-01
# %2012:00:00&finishdate=2017-08-04%2013:00:00&app_token=ag9zfnRlbGVmb25pL
# XRlc3RyHwsSElRlbmFudEFwcGxpY2F0aW9ucxiAgICw46OcCQyiARVzdGFnaW5nMS5h
# bG8tdGVjaC5jb20


@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/api", methods = ["GET", "POST"])
def api():
    if request.method == "POST":

        # get dates from index html
        main_startDate = request.form.get("startDate")
        main_startTime = request.form.get("startTime").replace(":", "")
        startDate = "{}{}{}{}".format(main_startDate ,"%", main_startTime , ":00:00")
        main_finishDate = request.form.get("finishDate")
        main_finishTime = request.form.get("finishTime").replace(":", "")
        finishDate = "{}{}{}{}".format(main_finishDate ,"%", main_finishTime , ":00:00")
        
        # get json data from api
        base_url = "https://staging1.alo-tech.com/api/?function=reportsCDRLogs&startdate=2017-08-01%2012:00:00&finishdate=2017-08-04%2013:00:00&"
        token = "app_token=ag9zfnRlbGVmb25pLXRlc3RyHwsSElRlbmFudEFwcGxpY2F0aW9ucxiAgICw46OcCQyiARVzdGFnaW5nMS5hbG8tdGVjaC5jb20"
        main_url = base_url + token
        response = requests.get(main_url)
        json_data = response.json()["CallList"]
      
        # filter data for layout into calltable
        def client_caller(callerAttribute):
            return [x[callerAttribute] for x in json_data]

        Calldate = client_caller("calldate")
        Called_num = client_caller("called_num")
        Callerid = client_caller("callerid")
        Answered = client_caller("answered")
        Duration = client_caller("duration")

        return render_template("calltable.html", Calldate = Calldate, Called_num = Called_num, Callerid = Callerid, Answered = Answered, Duration = Duration)
    else:
        return render_template("calltable.html")



     

# x = [x for x in json_verisi if x["calldate"] == "2017-08-03 14:38:31"]
# print(x)
        
   



@app.route("/calltable")
def callTable():
    return render_template("calltable.html")
    # if request.method == "POST":
       
    #     return render_template("calltable.html", startDate = startDate, finishDate = finishDate )
    # else:
    #     return render_template("calltable.html")


if __name__ == "__main__":
    app.run(debug = True) 