### SMTPlib MODULE ###
import smtplib

# Sender Info
my_email = "sample1@gmail.com"
password = "abc123"

### LONGWAY
# connection = smtplib.SMTP("smtp.gmail.com")
# #transport layer security - secures your connection to an email server
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.send_message(from_addr=my_email, 
#                         to_addrs="sample2@yahoo.com", 
#                         msg="Subject:Hello\n\nGood Afternoon.")
# connection.close()

### SHORTWAY
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.send_message(from_addr=my_email, 
                            to_addrs="sample2@yahoo.com", 
                            msg="Subject:Hello\n\nGood Afternoon.")


### datetime MODULE ###
import datetime as dt

# Find current date
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() # Returns num 0-7, mon-sun
print(day_of_week)


# Set a given date
date_of_birth = dt.datetime(year=2009,month=6, day=7, hour=4)
print(date_of_birth)


### random MODULE ###
import random

# Access "quotes.txt" file
with open("quotes.txt") as quote_file:
    # "readlines" - reads file line by line & stores each line as an item in a list 
    all_quotes = quote_file.readlines()
    
    # Retrieve random quote from list 
    quote = random.choice(all_quotes)

