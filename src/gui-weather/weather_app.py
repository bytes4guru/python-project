"""
Created on Aug 7, 2020
@author: Brennan Brown
"""

#===========
# IMPORTS
#===========
import tkinter as tk
from tkinter import Menu
from tkinter import ttk


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
tab_control = ttk.Notebook(win)         # Create Tab Control

tab_1 = ttk.Frame(tab_control)          # Create 1st Tab
tab_control.add(tab_1, text="Tab 1")    # Add 1st Tab
tab_2 = ttk.Frame(tab_control)          # Create 2nd Tab
tab_control.add(tab_2, text="Tab 2")    # Add 2nd Tab

tab_control.pack(expand=1, fill="both")
# ---------------------

# Container frame to hold all other widgets:
weather_frame = ttk.LabelFrame(tab_1, text=" Current Weather Conditions ")

# Tkinter grid layout manager:
weather_frame.grid(column=0, row=0, padx=8, pady=4)
weather_frame.grid_configure(column=0, row=1, padx=8, pady=4)

weather_cities_frame = ttk.LabelFrame(tab_1, text=" Latest Observations for: ")
weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(weather_cities_frame, text="Location:      ").grid(column=0, row=0)

city = tk.StringVar()
city_selected = ttk.Combobox(
    weather_cities_frame,
    width=24,
    textvariable=city)
city_selected["values"] = (
    "Los Angeles, CA",
    "Toronto, ON",
    "Rio de Janeiro, Brazil")
city_selected.grid(column=1, row=0)
city_selected.current(0)

for child in weather_cities_frame.winfo_children():
    child.grid_configure(padx=6, pady=6)

max_width = max([len(x) for x in city_selected["values"]])
new_width = max_width - 4
city_selected.config(width=new_width)

#==========================
ENTRY_WIDTH = max_width + 3
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

WEATHER_DATA = {
    "dewpoint_c": "16.7",
    "dewpoint_f": "62.1",
    "dewpoint_string": "62.1 F (16.7 C)",
    "icon_url_base": "http://forecast.weather.gov/images/wtf/small/",
    "icon_url_name": "nsct.png",
    "latitude": "33.93806",
    "location": "Los Angeles, Los Angelesalti International Airport, CA",
    "longitude": "-118.38889",
    "ob_url": "http://www.weather.gov/data/METAR/KLAX.1.txt",
    "observation_time": "Last Updated on Aug 7 2016, 9:53 pm PDT",
    "observation_time_rfc822": "Sun, 07 Aug 2016 21:53:00 -0700",
    "pressure_in": "29.81",
    "pressure_mb": "1009.1",
    "pressure_string": "1009.1 mb",
    "relative_humidity": "84",
    "station_id": "KLAX",
    "suggested_pickup": "15 minutes after the hour",
    "suggested_pickup_period": "60",
    "temp_c": "19.4",
    "temp_f": "67.0",
    "temperature_string": "67.0 F (19.4 C)",
    "two_day_history_url": "http://www.weather.gov/data/obhistory/KLAX.html",
    "visibility_mi": "9.00",
    "weather": "Partly Cloudy",
    "wind_degrees": "250",
    "wind_dir": "West",
    "wind_mph": "6.9",
    "wind_string": "West at 6.9 MPH (6 KT)"
}

UPDATED_DATA = WEATHER_DATA["observation_time"].replace("Last Updated on ", "")
updated.set(UPDATED_DATA)

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

#============
# START GUI
#============
win.mainloop()
