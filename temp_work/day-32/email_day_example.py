import random
import smtplib
import datetime as dt

MY_EMAIL = "helloworld@exmaple.com"
MY_PASSWORD = "****************"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.example.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="meme@example.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


"""
# my_email = "gspacetest001@gmail.com"
# password = "***********************"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="helloworld@yahoo.com.hk",
#         msg="Subject:Hello World\n\nThis is the body of my email."
#     )

# now = dt.datetime.now()
# year = now.year
# if year == 2022:
#     print("Yes")
# month = now.month
# day_of_week = now.weekday()
# print(now)
# print(day_of_week)
# 
# date_of_brith = dt.datetime(year=1995, month=12, day=15, hour=18, minute=24)
# print(date_of_brith)
"""



