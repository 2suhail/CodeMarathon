from datetime import datetime
import smtplib
import datetime as dt
import pandas
import random
MY_EMAIL = "YOUR_email"
MY_PASSWORD = "YOUR_pass"

def main():

# Check if today matches a birthday in the birthdays.csv
    today = dt.datetime.now()
    today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
    data = pandas.read_csv("birthdays.csv")
    birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if today_tuple in birthday_dict:
        birthday_person = birthday_dict[today_tuple]
        letter_file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
        with open(letter_file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])


# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, \
            to_addrs=birthday_person["email"], \
                msg=f"Subject:Happy Birthday! \n\n {contents}")

if __name__ == "__main__":
    main()