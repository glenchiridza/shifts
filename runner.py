# flask app start
from flask import Flask, render_template, url_for, request, redirect

from shift import generate_shift_schedule

import pickle
import datetime

app = Flask(__name__)

employees = [
    {"name": "Employee1", "shift_availability": ["morning"]},
    {"name": "Employee2", "shift_availability": ["night"]},
    {"name": "Employee3", "shift_availability": ["morning", "day", "night"]},
    {"name": "Employee4", "shift_availability": ["morning", "day", "night"]},
    {"name": "Employee5", "shift_availability": ["morning", "day", "night"]},
    {"name": "Employee6", "shift_availability": ["morning", "day", "night"]},
    {"name": "Employee7", "shift_availability": ["morning", "day", "night"]}
]

# Define the number of shifts per day and days per week
shifts_per_day = 3
days_per_week = 7


@app.route('/')
@app.route('/shifts')
def shifts():
    # get shuffled dates from saved file
    shifts_list = pickle.load(open("shifts.txt", "rb"))
    context = shifts_list

    return render_template("shifts.html", s1=context[0], s2=context[1], s3=context[2], date_list=context[3])


@app.route('/shuffle',methods=['GET','POST'])
def shuffle():
    if request.method == "POST":
        print("posted")
        generate_shift_schedule(employees, shifts_per_day, days_per_week)
        return redirect(url_for('shifts'))
    return render_template("shuffle_shifts.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
