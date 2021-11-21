# This program calculates the time passed since January 1, 1970, 00:00:00 (UTC).
# I don't acknowledge leap years in this program (first leap year in 1972, 12 in total from 1970)

import time
seconds = time.time()                       # Using time() method to get number of seconds from the beginning
minutes = seconds // 60                     # 1 minute is 60 seconds
hours = minutes // 60                       # 1 hour is 60 minutes
days = hours // 24                          # 1 day is 24 hours
years = int(days // 365)                    # 1 year is 365 days
days = int(days % 365)                      # % operator allows program to work with "leftover" from year and later with
hours = int(hours % 24)                     # hour,minute and seconds
minutes = int(minutes % 60)
seconds = int(seconds % 60)

print(years, "years,", days, "days,", hours, "hours,", minutes, " minutes and ", seconds, "seconds since the epoch.")

