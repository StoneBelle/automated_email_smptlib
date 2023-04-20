import datetime as dt
import pandas as pd 
import os
import random

##### PANDAS #####
class BirthDex:
    """Retrieves data from "birthdays.csv" file."""
    def __init__(self, file_name):
        super().__init__()

        # Reads "birthdays.csv" as pandas Dataframe
        self.sheet_data = pd.read_csv(file_name)
        self.num_rows = self.sheet_data.shape[0]


        # Retrieve name, email, and birthday data inside CSV file
        self.name_data = self.sheet_data["name"].tolist()
        self.email_data = self.sheet_data["email"].tolist()

    def birthday_data(self):
        """Returns a list[str] of all birthdays from the CSV file in the format of 'month/day'.'"""
        birth_month = self.sheet_data["month"].tolist()
        birth_day = self.sheet_data["day"].tolist()
        
        bday_data = []

        for x in range(len(birth_month)):
            if birth_month[x] <= 9:
                m = "0" + str(birth_month[x])
            else:
                m = str(birth_month[x])             
            bday_data.append(m + "/" + str(birth_day[x]))         
        
        return bday_data

test1 = BirthDex("birthdays.csv")
names = test1.name_data
emails = test1.email_data
bdays = test1.birthday_data()

##### DATETIME #####
# Get current date and store in variable
get_date = dt.datetime.now()
today = get_date.strftime("%D") # MM/DD/YY
year = str(get_date.year - 2000)

# Check if any birthdays match present date
for x in range(len(bdays)):
    check = bdays[x] + "/" + year
    # If dates match, open folder containing templates
    templates = []
    if check == today:
        print(check)
        path = "mail_templates/"
        template = random.choice(os.listdir(path))
        # for entry in os.listdir(path):
        #     if os.path.isfile(os.path.join(path, entry)):
        #         templates.append(entry)      
     
    else:
        print("No greetings need to be sent today.")

        # Select random template
        # Replace [NAME] with appropriate data from CSV file 


# Send updated template to person's email





# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
