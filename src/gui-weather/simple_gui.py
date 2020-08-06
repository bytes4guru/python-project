'''
Created on Aug 6, 2020
@author: Brennan Brown
'''

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
win.title("Simple GUI")

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
tab_control.add(tab_1, text="Tab 1")  # Add 1st Tab
tab_2 = ttk.Frame(tab_control)          # Create 2nd Tab
tab_control.add(tab_2, text="Tab 2")  # Add 2nd Tab

tab_control.pack(expand=1, fill="both")
# ---------------------

# Container frame to hold all other widgets:
x_frame = ttk.LabelFrame(tab_1, text=' Test Frame 1 ')

# Tkinter grid layout manager:
x_frame.grid(column=0, row=0, padx=8, pady=4)

# Adding a label:
ttk.Label(x_frame, text="Label: ").grid(
    column=0, row=0, sticky='W')
# ---------------------

test_label = tk.StringVar()
test_selected = ttk.Combobox(
    x_frame, width=12, textvariable=test_label)
# Create dictionary of values:
test_selected['values'] = ('Selection 1', 'Selection 2', 'Selection 3')
test_selected.grid(column=1, row=0)
test_selected.current(0)
# ---------------------

# Increase combobox to longest text
max_width = max([len(x) for x in test_selected['values']])
# Adjust for extra spacing:
new_width = max_width - 2
test_selected.config(width=new_width)

#==========================
ENTRY_WIDTH = max_width + 3
#==========================
# Adding Label and
# Textbox Entry Widgets
#==========================

ttk.Label(x_frame, text="Last Updated: ").grid(column=0, row=1, sticky='E')
updated = tk.StringVar()
updated_entry = ttk.Entry(x_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updated_entry.grid(column=1, row=1, sticky='W')

ttk.Label(x_frame, text="Weather: ").grid(
    column=0, row=2, sticky='E')
weather = tk.StringVar()
weather_entry = ttk.Entry(
    x_frame, width=ENTRY_WIDTH,
    textvariable=weather,
    state='readonly')
updated_entry.grid(
    column=1,
    row=2,
    sticky='W')

ttk.Label(x_frame, text="Temperature ").grid(
    column=0, row=3, sticky='E')
temperature = tk.StringVar()
temperature_entry = ttk.Entry(
    x_frame, width=ENTRY_WIDTH,
    textvariable=temperature,
    state='readonly')
temperature_entry.grid(
    column=1,
    row=3,
    sticky='W')

ttk.Label(x_frame, text="Dew Point: ").grid(
    column=0, row=4, sticky='E')
dew_point = tk.StringVar()
dew_point_entry = ttk.Entry(
    x_frame, width=ENTRY_WIDTH,
    textvariable=dew_point,
    state='readonly')
dew_point_entry.grid(
    column=1,
    row=4,
    sticky='W')

ttk.Label(x_frame, text="Relative Humidity: ").grid(
    column=0, row=5, sticky='E')
humidity = tk.StringVar()
humidity_entry = ttk.Entry(
    x_frame, width=ENTRY_WIDTH,
    textvariable=humidity,
    state='readonly')
humidity_entry.grid(
    column=1,
    row=5,
    sticky='W')

# Spacing around labels:
for child in x_frame.winfo_children():
    child.grid_configure(padx=4, pady=2)

#============
# START GUI
#============
win.mainloop()
