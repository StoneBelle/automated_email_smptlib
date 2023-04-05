# import smtplib

  
# # Sender Info
# my_email = "appbreweryinfo@gmail.com"
# password = "abcd1234()"


# # SHORTWAY
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.send_message(from_addr=my_email, 
#                             to_addrs="appbrewerytesting@yahoo.com", 
#                             msg="Subject:Hello\n\nGood Afternoon.")


### DATETIME MODULE ### 
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday() # Returns num 0-7, mon-sun


# date_of_birth = dt.datetime(year=2009,month=6, day=7, hour=4)
# print(date_of_birth)



### RANDOM MODULE ###
import random

# Open quote file
with open("quotes.txt") as quote_file:
    # Read file line by line
    all_quotes = quote_file.readlines()
    
    # Store each line from file as an item in a list 
    quote = random.choice(all_quotes)

    print(type(all_quotes))
    
 