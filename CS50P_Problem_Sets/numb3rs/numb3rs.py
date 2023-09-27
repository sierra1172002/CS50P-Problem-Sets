import re, sys


def main():

    print(validate(input("IPV4 Address: ").strip()))
    sys.exit()



def validate(ip):

    match = re.search(r"^((?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", ip)

    if match:
        return True
    else:
        return False



if __name__ == "__main__":
    main()