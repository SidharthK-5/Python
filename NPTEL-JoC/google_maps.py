"""
Program to plot map using google maps API
"""

import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(lat=23.2599, lng=77.4126, zoom=5)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

# Read the data from the csv file
with open("data/route.csv", "r") as file:
    reader = csv.reader(file)
    k = 0
    for row in reader:
        lat = float(row[0])
        lon = float(row[1])
        if k == 0:
            gmap.marker(lat, lon, color="yellow")
            k = 1
        else:
            gmap.marker(lat, lon, color="blue")

gmap.marker(lat, lon, color="red")
gmap.draw("data/map.html")
