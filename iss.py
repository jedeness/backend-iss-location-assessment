#!/usr/bin/env python

__author__ = 'Jed Enas with help from: Janelle Kuhns, Daniel Lomelino'

import turtle
import json
import time
import datetime
import requests

icon = "iss.gif"
map_gif = "map.gif"

def astro_list():
    r = requests.get('http://api.open-notify.org/astros.json')
    data = r.json()["people"]
    return data
    
def iss_location():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    location = r.json()["iss_position"]
    lat = float(location["latitude"])
    lon = float(location["longitude"])
    timestamp = r.json()["timestamp"]
    return lat, lon, timestamp

def create_map(lat, lon):
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.bgpic(map_gif)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape(icon)
    iss = turtle.Turtle()
    iss.shape(icon)
    iss.setheading(90)
    iss.penup()
    iss.goto(lon, lat)
    return screen
    
def plot_map(lat, lon):
    r = requests.get("http://api.open-notify.org/iss-pass.json", {"lat":lat, "lon":lon})
    r.raise_for_status()
    overhead_time = r.json()["response"][0]["risetime"]
    timestamp = time.ctime(overhead_time)
    location = turtle.Turtle()
    location.penup()
    location.color('yellow')
    location.goto(lon, lat)
    location.dot(5)
    location.write(timestamp)
    location.hideturtle()
    return timestamp


def main():
    # Part A
    astros = astro_list()
    for astro in astros:
        print(f"-{astro['name'], astro['craft']}")
    print(len(astros))
    
    # Part B
    iss_lat, iss_lon, _ = iss_location()
    
    # Part C
    create_map(iss_lat, iss_lon)
    plot_map(39.7684, -86.1581)

    turtle.done()

if __name__ == '__main__':
    main()
