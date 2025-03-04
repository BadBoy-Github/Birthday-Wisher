
import smtplib
import pandas as pd
import datetime as dt
import random

user = "sampgoogsamp@gmail.com"
password = "bfklzltmrygceswd"

day = dt.datetime.now().day
month = dt.datetime.now().month

data = pd.read_csv("birthdays.csv").to_dict(orient="records")
length = len(data)

bday_day = [data[i]["day"] for i in range(length)]
bday_month = [data[i]["month"] for i in range(length)]

if day in bday_day and month in bday_month:
    index = bday_day.index(day)
    name = data[index]["name"]
    email = data[index]["email"]
    letter = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])

    with open(f"letter_templates/{letter}") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user, password)
        connection.sendmail(from_addr=user, to_addrs=email, msg=f"Subject:Happy Birthday\n\n{letter}")