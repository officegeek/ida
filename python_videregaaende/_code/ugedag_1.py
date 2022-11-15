# Import
from datetime import date

# Input
date_input = input("Skriv dato (dd/mm/yyyy): ")

# Date
date_list = date_input.split("/")
day = int(date_list[0])
month = int(date_list[1])
year = int(date_list[2])
date_date = date(year, month, day)

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

# Print
day_of_week = days_of_week[n_day_of_week]
print(day_of_week)