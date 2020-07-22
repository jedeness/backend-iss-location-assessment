#!/usr/bin/env python

__author__ = 'Jed Enas'

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
    
def astro_location():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    location = r.json()["iss_position"]
    lat = float(location["latitude"])
    lon = float(location["longitude"])
    timestamp = r.json()["timestamp"]
    return lat, lon, timestamp

def create_map(lat, lon):
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgpic(map_gif)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape(icon)
    iss = turtle.Turtle()
    iss.shape(icon)
    iss.setheading(90)
    iss.penup()
    iss.goto(lat, lon)
    return screen
    
def plot_map(lat, lon):
    r = requests.get("http://api.open-notify.org/iss-pass.json", {"lat":lat, "lon":lon})
    r.raise_for_status()
    overhead_time = r.json()["response"][1]["risetime"]
    timestamps = time.ctime(overhead_time)
    location = turtle.Turtle()
    location.color('yellow')
    location.penup()
    location.goto(lat, lon)
    location.dot(25)
    location.hideturtle()
    location.write(timestamps)
    return timestamps


def main():
    # Part A
    astros = astro_list()
    for astro in astros:
        print(f"-{astro['name'], astro['craft']}")
    print(len(astros))
    
    # Part B
    # astro_loc = astro_location()
    # for loc in astro_loc:
    #     print(f"-{loc['latitude'], loc['longitude']}")
    # Part C

    print(astro_location())
    print(create_map(39, 86))


if __name__ == '__main__':
    main()
