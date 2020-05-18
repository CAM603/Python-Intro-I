"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

cur_year = datetime.now().year
cur_month = datetime.now().month

# args = sys.argv

# if len(args) == 3:
#   if(args[1])
#   month = int(args[1])
#   year = int(args[2])
#   print(calendar.month(year, month))
# elif len(args) == 2:
#   month = int(args[1])
#   print(calendar.month(cur_year, month))
# elif len(args) == 1:
#   print(calendar.month(cur_year, cur_month))
# else:
#   print("Just need a year and a month")
  
import argparse

my_parser = argparse.ArgumentParser(description="Please enter [month] [year]")
my_parser.add_argument("month", default=cur_month, type=int, choices=range(1, 13), nargs="?")
my_parser.add_argument("year", default=cur_year, type=int, choices=range(1900, cur_year + 1), nargs="?")

args = my_parser.parse_args()
print(calendar.month(args.year, args.month))