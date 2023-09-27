import re


def main():
    print(count(input("Text: ")))


def count(s):

    list = re.findall(r"\bum\b", s.lower())
    return len(list)


if __name__ == "__main__":
    main()