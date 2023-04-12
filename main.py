import datetime as dt
import pandas as pd 

# Get present date and store in variable

# Find current date and store in variable
today = dt.datetime.now()

# Current date as str
year = today.strftime("%Y") # 2023
month = today.strftime("%m") # April
day = today.strftime("%d") # 11
full_date = today.strftime("%D") # 04/11/23
weekday_short = today.strftime("%a") # Tue
weekday_full = today.strftime("%A") # Tuesday


print(full_date)
print(day)
print(weekday_full)


# Current time as str
hour = today.strftime("%H") # 23 (i.e. uses military time)
print(f"HOUR: {hour}")

# Current date as int
# year_int = today.year
# month_int = today.month
# day_int= today.weekday() # Returns num 0-7, mon-sun




# # Set a given date
# date_of_birth = dt.datetime(year=2009,month=6, day=7, hour=4)
# print(date_of_birth)









data = pd.Series([1,2,3])
print(data)
##################### Extra Hard Starting Project ######################


# Use panadas to retrieve name & birthday data from CSV file 

class BirthDex:
    def __init__(self, file_name):
        super().__init__()

        # Read "birthdays.csv"
        self.sheet_data = pd.read_csv(file_name)

        # For each person in CSV file, store name, email, and birthday inside nested dict
        self.name_data = self.sheet_data["name"].tolist()




test1 = BirthDex("birthdays.csv")
print(test1.name_data)



# Check if birthday matches present date

# If dates match, open folder containing templates

# Select random template

# Replace [NAME] with appropriate data from CSV file


# Send updated template to person's email





# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
