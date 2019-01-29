import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

"""
        This program is a Python Script that reads data from the files
        CO2.csv and temperature.csv and generates a labeled, nice plot of time vs CO2
        and time vs. temperature. It also takes as input an upper/lower threshold, and
        generates a figure chart of the CO2 emissions of all countries per capita
"""

def read_plot_temperature(month,start,end,lower,higher):
    """
        Plotting the temperature for a spesific month within a specified number
        of years.

        Args:
            month: the month to plot temperature from
            start: year to start ploting
            end: year to end ploting
            lower: minimum value for temperature to show in plot
            higher: maximum value for temperature to show in plot

        Saves figure as temperature_plot.jpg in static folder.
    """
    temperature=pd.read_csv('temperature.csv',sep=',')
    copy=temperature[['Year',month]]
    copy=copy[(copy['Year'] >= start)]
    copy=copy[(copy['Year'] <= end)]
    copy=copy[(copy[month] >= lower)]
    copy=copy[(copy[month] <= higher)]
    copy.plot(x='Year')
    plt.xlabel("Year")
    plt.ylabel("Temperature")
    plt.title("Temperature level")
    plt.savefig('static/temperature_plot.jpg')


def read_plot_co2(start,end,lower,higher):
    """
        Plotting CO2
        Args:
            start: year to start ploting
            end: year to end ploting
            lower: minimum value for temperature to show in plot
            higher: maximum value for temperature to show in plot

        Saves figure as co2_plot.jpg in static folder.
    """
    copy=pd.read_csv('co2.csv',sep=',')
    copy=copy[(copy['Year'] >= start)]
    copy=copy[(copy['Year'] <= end)]
    copy=copy[(copy['Carbon'] >= lower)]
    copy=copy[(copy['Carbon'] <= higher)]
    copy.plot(x ='Year')
    plt.savefig('static/co2_plot.jpg')

def read_co2_by_country_plot(year,lower_threshold,upper_threshold):
    """
        Plotting CO2 by country
        Args:
            year: year to plot for
            lower_threshold: minimum value for the country to be part of plot
            upper_threshold: maximum value for the country to be part of plot
        Saves figure as co2_by_country_plot.jpg in static folder.
    """
    country=pd.read_csv('CO2_by_country.csv',sep=',')
    copy=country[['Country Code','Indicator Name','Indicator Code',year]]
    copy=copy[(copy[year] >= lower_threshold)]
    copy=copy[(copy[year] <= upper_threshold)]
    copy.plot(x='Country Code', kind = 'bar')
    plt.savefig('static/co2_by_country_plot.jpg')


if __name__ == '__main__':
    month = 'February'
    start = 1900
    end = 1960
    lower = 0
    higher =  20000
    lower_threshold = 0
    upper_threshold = 10
    year = '2000'
    read_co2_by_country_plot(year,lower_threshold,upper_threshold)
    read_plot_co2(start,end,lower,higher)
    read_plot_temperature(month,start,end,lower,higher)
