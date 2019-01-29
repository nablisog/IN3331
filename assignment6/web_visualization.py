from temperature_co2_plotter import read_plot_temperature, read_co2_by_country_plot, read_plot_co2
from flask import Flask
from flask import render_template
from flask import url_for, request
"""
    This program is a Python Script that uses the script from temperature_co2_plotter.py
    to generate a plot of temperature vs. Time(years) and a plot of CO2 vs time(years)
    and display it on the web page(http://localhost:5000/)

    You might need to clear cache between uses. 
"""

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature')
def temperature():
    read_plot_temperature(month,start,end,lower,higher)
    return render_template('temperature.html')

@app.route('/co2')
def co2():
    read_plot_co2(start,end,lower,higher)
    return render_template('co2.html')

@app.route('/co2_by_country')
def co2_by_country():
    read_co2_by_country_plot(year,lower_threshold,upper_threshold)
    return render_template('co2_by_country.html')

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    month = 'February'
    start = 1900
    end = 1970
    lower = 0
    higher =  20000
    lower_threshold = 0
    upper_threshold = 10
    year = '2000'
    app.run(debug=True)
