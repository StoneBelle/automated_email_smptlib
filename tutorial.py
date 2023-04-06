import random
import smtplib
import datetime as dt


# Determine if present date matches email date
today = dt.datetime.now()
year = today.year
month = today.month
day = today.weekday() # Returns num 0-7, mon-sun


email_day = dt.datetime(year=2023, month=4, day=0, hour=8)
print(email_day)

# Access quotes.txt file
with open("quotes.txt") as quote_file:
    # "readlines" - reads file line by line & stores each line as an item in a list 
    all_quotes = quote_file.readlines()
    
    # Retrieve random quote from list 
    quote = random.choice(all_quotes)
 

 
# Sender Info
s_email = "yyyyyyyyy@yyyy.com"
s_password = "thisisapassword"

## Set up SMTPlib for sending & recieving emails
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=s_email, password=s_password)
    connection.send_message(from_addr=s_email, 
                            to_addrs="xxxxxxxx@xxxxx.com", 
                            msg="Subject:{quote}.")
