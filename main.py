from flask import Flask, redirect, request, render_template, url_for
from datetime import datetime
import time

#This Python flask app works out the number of days 
#between two selected dates on a windows form 
#App written by Paul Coke (c)2024

app = Flask(__name__)



@app.route("/",methods=['GET','POST'])
def home():
    global date_from, date_to
    #When the user selects and submits the date values on the form
    #we grab the date values, then pass them to the "date_difference"
    #method, to work out the total number of days
    if request.method == "POST":
        date_from = request.form['dateFrom']
        date_to = request.form['dateTo']
        total_days = date_difference(date_from, date_to)
        return render_template("result.html", total_days=total_days)
    
    return render_template("index.html")
    

#This method takes two date arguments
#and works out the number of days between 
#the two dates specified
def date_difference(date_f, date_t):
    date_f = date_from
    date_t = date_to
    date1 = datetime.strptime(date_f,"%Y-%m-%d")
    date2 = datetime.strptime(date_t,"%Y-%m-%d")

    delta = abs(date2 - date1)
    return delta.days




if __name__ == "__main__":
    app.run(debug=True)

