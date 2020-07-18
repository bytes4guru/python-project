# line_reader.py

import os

# Function: Will read and return the first line from a file. 
# The filename and path to this pile will be passed in as 
# an argument to the function, and the function will open 
# that file, read in the first line, and return it.
def read_from_file(filename):
	if not os.path.exists(filename):
		raise Exception("Error: File Not Found.")
	infile = open(filename, "r")
	line = infile.readline()
	return line