# Import
import argparse
import sys
from datetime import date

# Input
parser = argparse.ArgumentParser(description="Get day of the week from a date")

parser.add_argument("date", nargs="?", help="Date (mm/dd/yyyy)", default=None)

arguments = parser.parse_args()

use_arguments = True if arguments.date is not None else False

# Date - med error handling
while True:
    if use_arguments:
        date_input = arguments.date
    else:
        date_input = input("Skriv dato (dd/mm/yyyy): ")
 
    try:
        date_list = date_input.split("/")
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
 
        date_date = date(year, month, day)
    except:
        print("Invalid date")
        if use_arguments:
            sys.exit()
        continue
 
    break

n_day_of_week = date_date.weekday()

# Ugedage - navne DK
days_of_week = (
    "Mandag",
    "Tirsdag",
    "Onsdag",
    "Torsdag",
    "Fredag",
    "Lørdag",
    "Søndag",
)

day_of_week = days_of_week[n_day_of_week]
print(day_of_week)