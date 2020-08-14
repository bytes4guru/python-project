"""
Created on Aug 13, 2020
@author: Brennan Brown
"""

#===========
# IMPORTS
#===========
from API_key import OWM_API_KEY

from datetime import datetime

import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext

import urllib.request
from urllib.request import urlopen
import xml.etree.ElementTree as ET

from html.parser import HTMLParser

import PIL.Image
import PIL.ImageTk

from pprint import pprint

import json

#============
# FUNCTIONS
#============

# Exit GUI Cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()


#============
# PROCEDURAL
#============

# Create instance:
win = tk.Tk()

# Add a title:
win.title("Weather App")

# ---------------------
# Creating a Menu Bar
menu_bar = Menu()
win.config(menu=menu_bar)

# Add Menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(
    label="Exit", command=_quit)
menu_bar.add_cascade(
    label="File", menu=file_menu)

# Add a Secondary Menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(
    label="Help", menu=help_menu)
# ---------------------

# Tab Control / Notebook
tab_control = ttk.Notebook(win)
tab_1 = ttk.Frame(tab_control)
tab_control.add(tab_1, text="NOAA")
tab_2 = ttk.Frame(tab_control)
tab_control.add(tab_2, text="Station Lookup")
tab_3 = ttk.Frame(tab_control)
tab_control.add(tab_3, text="Images")
tab_4 = ttk.Frame(tab_control)
tab_control.add(tab_4, text="OpenWeather")

tab_control.pack(expand=1, fill="both")
# ---------------------

# Container frame to hold all other widgets:
weather_frame = ttk.LabelFrame(
    tab_1, text=" Current Weather Conditions ")

# Tkinter grid layout manager:
weather_frame.grid(
    column=0, row=0, padx=8, pady=4)
weather_frame.grid_configure(
    column=0, row=1, padx=8, pady=4)

weather_cities_frame = ttk.LabelFrame(
    tab_1, text=" Latest Observation for ")
weather_cities_frame.grid(
    column=0, row=0, padx=8, pady=4)
ttk.Label(
    weather_cities_frame, text="Weather Station ID: ").grid(column=0, row=0)

#==========================
ENTRY_WIDTH = 22
#==========================
# Adding Label and
# Textbox Entry Widgets
#==========================

ttk.Label(weather_frame, text="Last Updated: ").grid(
    column=0,
    row=1,
    sticky="E")
updated = tk.StringVar()
updated_entry = ttk.Entry(
    weather_frame,
    width=ENTRY_WIDTH,
    textvariable=updated,
    state="readonly")
updated_entry.grid(
    column=1,
    row=1,
    sticky="W")

ttk.Label(weather_frame, text="Weather: ").grid(
    column=0, row=2, sticky="E")
weather_desc = tk.StringVar()
weather_entry = ttk.Entry(
    weather_frame,
    width=ENTRY_WIDTH,
    textvariable=weather_desc,
    state="readonly")
weather_entry.grid(
    column=1,
    row=2,
    sticky="W")

ttk.Label(weather_frame, text="Temperature: ").grid(
    column=0, row=3, sticky="E")
temperature = tk.StringVar()
temperature_entry = ttk.Entry(
    weather_frame,
    width=ENTRY_WIDTH,
    textvariable=temperature,
    state="readonly")
temperature_entry.grid(
    column=1,
    row=3,
    sticky="W")

ttk.Label(weather_frame, text="Dew Point: ").grid(
    column=0, row=4, sticky="E")
dew_point = tk.StringVar()
dew_point_entry = ttk.Entry(
    weather_frame,
    width=ENTRY_WIDTH,
    textvariable=dew_point,
    state="readonly")
dew_point_entry.grid(
    column=1,
    row=4,
    sticky="W")

ttk.Label(weather_frame, text="Relative Humidity: ").grid(
    column=0, row=5, sticky="E")
humidity = tk.StringVar()
humidity_entry = ttk.Entry(
    weather_frame,
    width=ENTRY_WIDTH,
    textvariable=humidity,
    state="readonly")
humidity_entry.grid(
    column=1,
    row=5,
    sticky="W")

ttk.Label(weather_frame, text="Wind: ").grid(
    column=0,
    row=6,
    sticky="E")
wind = tk.StringVar()
wind_entry = ttk.Entry(
    weather_frame,
    width=ENTRY_WIDTH,
    textvariable=wind,
    state="readonly")
wind_entry.grid(
    column=1,
    row=6,
    sticky="W")

ttk.Label(weather_frame, text="Visibility: ").grid(
    column=0,
    row=7,
    sticky="E")
visibility = tk.StringVar()
visibility_entry = ttk.Entry(
    weather_frame,
    width=ENTRY_WIDTH,
    textvariable=visibility,
    state="readonly")
visibility_entry.grid(
    column=1,
    row=7,
    sticky="W")

ttk.Label(weather_frame, text="MSL Pressure: ").grid(
    column=0,
    row=8,
    sticky="E")
pressure = tk.StringVar()
pressure_entry = ttk.Entry(
    weather_frame,
    width=ENTRY_WIDTH,
    textvariable=pressure,
    state="readonly")
pressure_entry.grid(
    column=1,
    row=8,
    sticky="W")

ttk.Label(weather_frame, text="Altimeter: ").grid(
    column=0,
    row=9,
    sticky="E")
altimeter = tk.StringVar()
altimeter_entry = ttk.Entry(
    weather_frame,
    width=ENTRY_WIDTH,
    textvariable=altimeter,
    state="readonly")
altimeter_entry.grid(
    column=1,
    row=9,
    sticky="W")

# Spacing around labels:
for child in weather_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)


#========================================================
# NOAA (National Oceanic and Atmospheric Administration)
#========================================================

station_id = tk.StringVar()
station_id_combo = ttk.Combobox(
    weather_cities_frame,
    width=6,
    textvariable=station_id)
station_id_combo["values"] = ("KLAX", "KDEN", "KNYC")
station_id_combo.grid(column=1, row=0)
station_id_combo.current(0)

def _get_station():
    station = station_id_combo.get()
    get_weather_data(station)
    populate_gui()

get_weather_btn = ttk.Button(
    weather_cities_frame,
    text="Get Weather",
    command=_get_station).grid(column=2, row=0)

# Station City label
location = tk.StringVar()
ttk.Label(weather_cities_frame, textvariable=location).grid(
    column=0,
    row=1,
    columnspan=3)
for child in weather_cities_frame.winfo_children():
    child.grid_configure(padx=5, pady=4)

WEATHER_DATA = {
    "observation_time": "",
    "weather": "",
    "temp_f":  "",
    "temp_c":  "",
    "dewpoint_f": "",
    "dewpoint_c": "",
    "relative_humidity": "",
    "wind_string":   "",
    "visibility_mi": "",
    "pressure_string": "",
    "pressure_in": "",
    "location": ""
}

def get_weather_data(station_id):
    url_general = "http://www.weather.gov/xml/current_obs/{}.xml"
    url = url_general.format(station_id)
    print(url)
    request = urllib.request.urlopen(url)
    content = request.read().decode()
    print(content)

    # Using ElementTree to retreive specific tags from .XML
    xml_root = ET.fromstring(content)
    print("xml_root: {}\n".format(xml_root.tag))

    for data_point in WEATHER_DATA.keys():
        WEATHER_DATA[data_point] = xml_root.find(data_point).text

def populate_gui():
    location.set(WEATHER_DATA["location"])
    updated.set(WEATHER_DATA["observation_time"].replace("Last Updated on ", ""))
    weather_desc.set(WEATHER_DATA["weather"])
    temperature.set("{} \xb0F  ({} \xb0C)".format(
        WEATHER_DATA["temp_f"],
        WEATHER_DATA["temp_c"]))
    dew_point.set("{} \xb0F  ({} \xb0C)".format(
        WEATHER_DATA["dewpoint_f"],
        WEATHER_DATA["dewpoint_c"]))
    humidity.set(WEATHER_DATA["relative_humidity"] + " %")
    wind.set(WEATHER_DATA["wind_string"])
    visibility.set(WEATHER_DATA["visibility_mi"] + " miles")
    pressure.set(WEATHER_DATA["pressure_string"])
    altimeter.set(WEATHER_DATA["pressure_in"] + " in Hg")


#==============
# STATION DATA
#==============

weather_states_frame = ttk.LabelFrame(tab_2, text=" Weather Station IDs ")
weather_states_frame.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(weather_states_frame, text="Select a State: ").grid(column=0, row=0)

state = tk.StringVar()
state_combo = ttk.Combobox(weather_states_frame, width=5, textvariable=state)
state_combo["values"] = (
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI",
    "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI",
    "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC",
    "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
    "VT", "VA", "WA", "WV", "WI", "WY")

state_combo.grid(column=1, row=0)
state_combo.current(0)

def _get_cities():
    state = state_combo.get()
    get_city_station_ids(state)

get_weather_btn = ttk.Button(
    weather_states_frame,
    text="Get Cities",
    command=_get_cities).grid(column=2, row=0)

scroll = scrolledtext.ScrolledText(
    weather_states_frame,
    width=38,
    height=17,
    wrap=tk.WORD)
scroll.grid(column=0, row=1, columnspan=3)

for child in weather_states_frame.winfo_children():
    child.grid_configure(padx=6, pady=6)

def get_city_station_ids(state):
    # Retrieves HTML, not XML
    url_general = "http://w1.weather.gov/xml/current_obs/seek.php?state={}&Find=Find"
    state = state.lower()
    url = url_general.format(state)
    request = urllib.request.urlopen(url)
    content = request.read().decode()
    parser = WeatherHTMLParser()
    parser.feed(content)

    # Verify amount of stations vs. cities
    print(len(parser.stations) == len(parser.cities))
    # Clear scrolledText widget for next btn click
    scroll.delete("1.0", tk.END)

    for idx in range(len(parser.stations)):
        city_station = parser.cities[idx] + " (" + parser.stations[idx] + ")"
        print(city_station)
        scroll.insert(tk.INSERT, city_station + "\n")

class WeatherHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stations = []
        self.cities = []
        self.grab_data = False

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if "display.php?stid=" in str(attr):
                cleaned_attr = str(attr).replace("('href', 'display.php?stid=", '').replace("')", '')
                self.stations.append(cleaned_attr)
                self.grab_data = True

    def handle_data(self, data):
        if self.grab_data:
            self.cities.append(data)
            self.grab_data = False


#========
# IMAGES
#========

weather_images_frame = ttk.LabelFrame(tab_3, text=' Weather Images ')
weather_images_frame.grid(column=0, row=0, padx=8, pady=4)

img = PIL.Image.open("few_clouds.png")
photo = PIL.ImageTk.PhotoImage(img)
ttk.Label(weather_images_frame, image=photo).grid(column=0, row=0)

img = PIL.Image.open("night_few_clouds.png")
photo1 = PIL.ImageTk.PhotoImage(img)
ttk.Label(weather_images_frame, image=photo1).grid(column=1, row=0)

img = PIL.Image.open("night_fair.png")
photo2 = PIL.ImageTk.PhotoImage(img)
ttk.Label(weather_images_frame, image=photo2).grid(column=2, row=0)


#====================
# OpenWeatherMap API
#====================

open_weather_cities_frame = ttk.LabelFrame(tab_4, text=' Latest Observation for ')
open_weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

open_location = tk.StringVar()
ttk.Label(open_weather_cities_frame, textvariable=open_location).grid(column=0, row=1, columnspan=3)

ttk.Label(open_weather_cities_frame, text="City: ").grid(column=0, row=0)

open_city = tk.StringVar()
open_city_combo = ttk.Combobox(open_weather_cities_frame, width=16, textvariable=open_city)
open_city_combo['values'] = ('Los Angeles, US', 'London, UK', 'Paris, FR', 'Mumbai, IN', 'Beijing, CN')
open_city_combo.grid(column=1, row=0)
open_city_combo.current(0)

def _get_station_open():
    city = open_city_combo.get()
    get_open_weather_data(city)
get_weather_btn = ttk.Button(
    open_weather_cities_frame,
    text='Get Weather',
    command=_get_station_open).grid(column=2, row=0)

for child in open_weather_cities_frame.winfo_children():
        child.grid_configure(padx=5, pady=2)

open_frame = ttk.LabelFrame(tab_4, text=' Current Weather Conditions ')
open_frame.grid(column=0, row=1, padx=8, pady=4)

#================
ENTRY_WIDTH = 25
#================
# Adding Label & Textbox Entry widgets
#---------------------------------------------
ttk.Label(open_frame, text="Last Updated:").grid(
    column=0,
    row=1,
    sticky='E')
open_updated = tk.StringVar()
open_updatedEntry = ttk.Entry(
    open_frame,
    width=ENTRY_WIDTH,
    textvariable=open_updated,
    state='readonly')
open_updatedEntry.grid(
    column=1,
    row=1,
    sticky='W')

ttk.Label(open_frame, text="Weather:").grid(
    column=0,
    row=2,
    sticky='E')
open_weather = tk.StringVar()
open_weatherEntry = ttk.Entry(
    open_frame,
    width=ENTRY_WIDTH,
    textvariable=open_weather,
    state='readonly')
open_weatherEntry.grid(
    column=1,
    row=2,
    sticky='W')

ttk.Label(open_frame, text="Temperature:").grid(
    column=0,
    row=3,
    sticky='E')
open_temp = tk.StringVar()
open_tempEntry = ttk.Entry(
    open_frame,
    width=ENTRY_WIDTH,
    textvariable=open_temp,
    state='readonly')
open_tempEntry.grid(
    column=1,
    row=3,
    sticky='W')

ttk.Label(open_frame, text="Relative Humidity:").grid(
    column=0,
    row=5,
    sticky='E')
open_rel_humi = tk.StringVar()
open_rel_humiEntry = ttk.Entry(
    open_frame,
    width=ENTRY_WIDTH,
    textvariable=open_rel_humi,
    state='readonly')
open_rel_humiEntry.grid(
    column=1,
    row=5,
    sticky='W')

ttk.Label(open_frame, text="Wind:").grid(
    column=0,
    row=6,
    sticky='E')
open_wind = tk.StringVar()
open_windEntry = ttk.Entry(
    open_frame,
    width=ENTRY_WIDTH,
    textvariable=open_wind,
    state='readonly')
open_windEntry.grid(
    column=1,
    row=6,
    sticky='W')

ttk.Label(open_frame, text="Visibility:").grid(
    column=0,
    row=7,
    sticky='E')
open_visi = tk.StringVar()
open_visiEntry = ttk.Entry(
    open_frame,
    width=ENTRY_WIDTH,
    textvariable=open_visi,
    state='readonly')
open_visiEntry.grid(
    column=1,
    row=7,
    sticky='W')

ttk.Label(open_frame, text="Pressure:").grid(
    column=0,
    row=8,
    sticky='E')
open_msl = tk.StringVar()
open_mslEntry = ttk.Entry(
    open_frame,
    width=ENTRY_WIDTH,
    textvariable=open_msl,
    state='readonly')
open_mslEntry.grid(
    column=1,
    row=8,
    sticky='W')

ttk.Label(open_frame, text="Sunrise:").grid(
    column=0,
    row=9,
    sticky='E')
sunrise = tk.StringVar()
sunriseEntry = ttk.Entry(
    open_frame,
    width=ENTRY_WIDTH,
    textvariable=sunrise,
    state='readonly')
sunriseEntry.grid(
    column=1,
    row=9,
    sticky='E')

ttk.Label(open_frame, text="Sunset:").grid(
    column=0,
    row=10,
    sticky='E')
sunset = tk.StringVar()
sunsetEntry = ttk.Entry(
    open_frame,
    width=ENTRY_WIDTH,
    textvariable=sunset,
    state='readonly')
sunsetEntry.grid(
    column=1,
    row=10,
    sticky='E')

for child in open_frame.winfo_children():
        child.grid_configure(padx=4, pady=2)


#================================
# OpenWeatherMap Data Collection
#================================

def get_open_weather_data(city):
    city = city.replace(' ', '%20')
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, OWM_API_KEY)
    response = urlopen(url)
    data = response.read().decode()
    json_data = json.loads(data)

    pprint(json_data)

    lastupdate_unix = json_data['dt']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    temp_kelvin = json_data['main']['temp']
    city_name = json_data['name']
    city_country = json_data['sys']['country']
    sunrise_unix = json_data['sys']['sunrise']
    sunset_unix = json_data['sys']['sunset']
    owm_weather = json_data['weather'][0]['description']
    weather_icon = json_data['weather'][0]['icon']
    wind_deg = json_data['wind']['deg']
    wind_speed_meter_sec = json_data['wind']['speed']

    try: visibility_meter = json_data['visibility']
    except: visibility_meter = 'N/A'

    def kelvin_to_celsius(temp_k):
        return "{:.1f}".format(temp_k - 273.15)

    def kelvin_to_fahrenheit(temp_k):
        return "{:.1f}".format((temp_k - 273.15)* 1.8000 + 32.00)

    def unix_to_datetime(unix_time):
        return datetime.fromtimestamp(int(unix_time)
        ).strftime('%Y-%m-%d %H:%M:%S')

    def meter_to_miles(meter):
        return "{:.2f}".format((meter * 0.00062137))

    if visibility_meter is 'N/A':
        visibility_miles = 'N/A'
    else:
        visibility_miles = meter_to_miles(visibility_meter)

    def mps_to_mph(meter_second):
        return "{:.1f}".format((meter_second * (2.23693629)))

    # -------------------------------------------------------
    # Update GUI entry widgets with live data
    open_location.set('{}, {}'.format(city_name, city_country))

    lastupdate = unix_to_datetime(lastupdate_unix)
    open_updated.set(lastupdate)
    open_weather.set(owm_weather)
    temp_fahr = kelvin_to_fahrenheit(temp_kelvin)
    temp_cels = kelvin_to_celsius(temp_kelvin)
    open_temp.set('{} \xb0F  ({} \xb0C)'.format(temp_fahr, temp_cels))
    open_rel_humi.set('{} %'.format(humidity))
    wind_speed_mph = mps_to_mph(wind_speed_meter_sec)
    open_wind.set('{} degrees at {} MPH'.format(wind_deg, wind_speed_mph))
    open_visi.set('{} miles'.format(visibility_miles))
    open_msl.set('{} hPa'.format(pressure))
    sunrise_dt = unix_to_datetime(sunrise_unix)
    sunrise.set(sunrise_dt)
    sunset_dt = unix_to_datetime(sunset_unix)
    sunset.set(sunset_dt)

    print(weather_icon)
    url_icon = "http://openweathermap.org/img/w/{}.png".format(weather_icon)
    ico = urlopen(url_icon)
    open_im = PIL.Image.open(ico)
    open_photo = PIL.ImageTk.PhotoImage(open_im)
    ttk.Label(open_weather_cities_frame, image=open_photo).grid(column=0, row=1)
    win.update()


#============
# START GUI
#============
win.mainloop()
