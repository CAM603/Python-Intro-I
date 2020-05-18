"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import os
import sys
# YOUR CODE HERE
# def read():
#     text_file = open("/Users/cameronhawley/Documents/Computer Science/Python-Intro-I/src/foo.txt", "r")
#     print(text_file.read())
#     text_file.close()
# read()
# with open("/Users/cameronhawley/Documents/Computer Science/Python-Intro-I/src/foo.txt", "r") as file:
#     data = file.read()
#     print(data)

with open(os.path.join(sys.path[0], "foo.txt"), "r") as file:
    data = file.read()
    print(data)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
def write():
    new_file = open("/Users/cameronhawley/Documents/Computer Science/Python-Intro-I/src/new.txt", "r+")
    new_file.write("What kind of black magic is this?")
    new_file.close()
write()

# YOUR CODE HERE