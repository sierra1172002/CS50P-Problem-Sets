import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):

    if match := re.search(r"^(1[1-2]|[1-9])(:[0-5][0-9])?\s(AM|PM)\sto\s(1[1-2]|[1-9])(:[0-5][0-9])?\s(AM|PM)$", s):
        t1 = int(match[1])
        t2 = match[2]
        t3 = match[3]
        t4 = int(match[4])
        t5 = match[5]
        t6 = match[6]

        if t3 == "AM" and t1 == 12:
            t1 = 0
        elif t3 == "PM" and t1 != 12:
            t1 += 12

        if t6 == "AM" and t4 == 12:
            t4 = 0
        elif t6 == "PM" and t4 != 12:
            t4 += 12

        if t2 == None and t5 == None:
            return (f"{t1:02}:00 to {t4:02}:00")
        else:
            return (f"{t1:02}{t2} to {t4:02}{t5}")
    else:
        raise ValueError




if __name__ == "__main__":
    main()