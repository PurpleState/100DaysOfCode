import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

MY_EMAIL = "$$$$@gmail.com"
MY_PASSWORD = "****"

if weekday == 0:

    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="$$$$$$$$$$@yahoo.com",
            msg=f"Subject:Monday Motivation :)\n\n{quote}"
        )
