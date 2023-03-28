# import smtplib


# # Sender Info
# my_email = "appbreweryinfo@gmail.com"
# password = "abcd1234()"

# # LONGWAY
# # connection = smtplib.SMTP("smtp.gmail.com")


# # #transport layer security - secures your connection to an email server
# # connection.starttls()
# # connection.login(user=my_email, password=password)
# # connection.send_message(from_addr=my_email, 
# #                         to_addrs="appbrewerytesting@yahoo.com", 
# #                         msg="Subject:Hello\n\nGood Afternoon.")
# # connection.close()

# # SHORTWAY
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.send_message(from_addr=my_email, 
#                             to_addrs="appbrewerytesting@yahoo.com", 
#                             msg="Subject:Hello\n\nGood Afternoon.")


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() # Returns num 0-7, mon-sun



print(day_of_week)

date_of_birth = dt.datetime(year=2009,month=6, day=7, hour=4)

print(date_of_birth)