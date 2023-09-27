from datetime import date
import sys, re
from inflect import engine



def main():

    d = input("Date of birth: ").strip()

    #date_check = re.search(r"[0-9]+-(1[0-2]|0[1-9])-(3[0-1]|2[0-9]|1[0-9]|0[1-9])", d)
    date_check = re.search(r"^[0-9]+-[0-9]+-[0-9]+$",d)

    if date_check:

        year, month, day = d.split("-")

        year, month, day = int(year), int(month), int(day)

    else:
        sys.exit("Invalid Date")

    print(age_minutes(year, month, day))


def age_minutes(year, month, day):

    try:
        birth_date = date(year, month, day)

        age = date.today() - birth_date
        age_min = age.days*60*24
        age_min_words = engine().number_to_words(age_min, andword="")
        return f"{age_min_words.capitalize()} minutes"

    except ValueError:
        return "Invalid Date"



if __name__ == "__main__":
    main()

