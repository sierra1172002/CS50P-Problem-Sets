def main():

    convert_date()


def convert_date():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:

        user_date = input("Date: ")

        if '/' in user_date:
            m, d, y = user_date.split("/")
        elif "," in user_date:
            user_date = user_date.replace(",","")
            m, d, y = user_date.split(" ")
            if m in months:
                m = months.index(m) + 1

        try:
            if 0 > int(m) or 0 > int(d) or 12 < int(m) or int(d) > 31:
                continue
            else:
                break
        except (ValueError, Exception):
            continue



    print(f"{int(y)}" + "-" + f"{int(m):02}" + "-" + f"{int(d):02}")



main()


