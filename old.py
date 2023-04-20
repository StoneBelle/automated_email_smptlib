import datetime as dt
import pandas as pd 


# Get current date and store in variable
today = dt.datetime.now()

# Current date as str (i.e. "strf" == string format)
year = today.strftime("%Y") # 2023
month = today.strftime("%m") # April
day = today.strftime("%d") # 11
full_date = today.strftime("%D") # 04/11/23
weekday_short = today.strftime("%a") # Tue
weekday_full = today.strftime("%A") # Tuesday

# Current miliarty time as str 
hour = today.strftime("%H") 
minute = today.strftime("%M") 
second = today.strftime("%S")
print(second)


# Current date as int
# year_int = today.year
# month_int = today.month
# day_int= today.weekday() # Returns num 0-7, mon-sun