import datetime as dt
import pandas as pd 
import os
import random
import smtplib

class BirthDex: 
    """Retrieves data from "birthdays.csv" file and sends out a personal birthday email if it's someone's birthday."""
    def __init__(self, file_name):
        super().__init__()

        # Reads "birthdays.csv" as pandas Dataframe
        self.sheet_data = pd.read_csv(file_name)
   
        # Stores all name and email data from CSV file into a list
        self.name_data = self.sheet_data["name"].tolist()
        self.email_data = self.sheet_data["email"].tolist()

    # Modifies birthdates to following format: MM/DD/YY
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

check_birthdays = BirthDex("birthdays.csv")
names = check_birthdays.name_data
emails = check_birthdays.email_data
bdays = check_birthdays.birthday_data()

# Present date
get_date = dt.datetime.now()
today = get_date.strftime("%D") # MM/DD/YY
year = str(get_date.year - 2000)

# Checks if any birthdays match present date
for x in range(len(bdays)):
    check = bdays[x] + "/" + year
    # Open templates folder if match found
    if check == today:
        # Selects a random template from fodler 
        path = "mail_templates/"
        template = random.choice(os.listdir(path))    
        pathway = path + template 

        # Opens the chosen template
        with open(pathway, "r") as temp:
            draft = temp.read()
            print(draft)
        
        # Replaces [NAME] with appropriate data from CSV file 
        with open(pathway, "w") as temp:
            final_draft = draft.replace("[NAME]", names[x])
            print(final_draft)

        # Sender Info
        sender = "sample1@gmail.com"
        password = "abc123"

        # Sends updated email draft to reciever 
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() # Secures connection to email server
            connection.login(user=sender, password=password)
            connection.send_message(from_addr=sender, 
                                    to_addrs=emails[x], 
                                    msg=f"Subject:Happy Birthday! :D\n\n{final_draft}.")
            