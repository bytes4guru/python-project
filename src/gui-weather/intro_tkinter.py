#=========
# Imports
#=========
# Python 3: "t" lowercase
import tkinter as tk
# Create instance:
win = tk.Tk()

# Add title:
win.title("Python GUI")


#===========
# Functions
#===========

def get_current_windows_size():
    # Gets runtime size
    win.update()
    print("Width: ", win.winfo_width())
    print("Height: ", win.winfo_height())

def increase_window_width():
    # Value 1 is default
    win.minsize(width = 300, height = 1)
    # Disables reszing the GUI entirely
    win.resizable(0, 0)


#===========
# Start GUI
#===========
get_current_windows_size()
increase_window_width()
print()
get_current_windows_size()

win.mainloop()