"""
Created on Aug 13, 2020
@author: Brennan Brown
"""

#===========
# IMPORTS
#===========
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext

import urllib.request
import xml.etree.ElementTree as ET

from html.parser import HTMLParser

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
tab_control = ttk.Notebook(win)           # Create Tab Control
tab_1 = ttk.Frame(tab_control)
tab_control.add(tab_1, text="Weather")    # Add 1st Tab
tab_2 = ttk.Frame(tab_control)
tab_control.add(tab_2, text="Locations")  # Add 2nd Tab
tab_3 = ttk.Frame(tab_control)
tab_control.add(tab_3, text="Images")     # Add 3rd Tab

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

# We are creating a container frame to hold all other widgets
weather_images_frame = ttk.LabelFrame(tab_3, text=' Weather Images ')
weather_images_frame.grid(column=0, row=0, padx=8, pady=4)        

# ---------------------------------------------------------------
# requires Pillow (PIL in Python 2.x)
import PIL.Image
import PIL.ImageTk

im = PIL.Image.open("few_clouds.png")
photo = PIL.ImageTk.PhotoImage(im)
ttk.Label(weather_images_frame, image=photo).grid(column=0, row=0) 

im = PIL.Image.open("night_few_clouds.png")
photo1 = PIL.ImageTk.PhotoImage(im)
ttk.Label(weather_images_frame, image=photo1).grid(column=1, row=0) 

im = PIL.Image.open("night_fair.png")
photo2 = PIL.ImageTk.PhotoImage(im)
ttk.Label(weather_images_frame, image=photo2).grid(column=2, row=0) 


#============
# START GUI
#============
win.mainloop()
