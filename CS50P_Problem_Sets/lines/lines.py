import sys

def main():

    count_lines(get_file_name())


def get_file_name():

    if len(sys.argv) < 2:
        sys.exit("Too few command-lin arguments.")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-lin arguments.")
    elif sys.argv[1][-3:] == ".py" and len(sys.argv) == 2:
        file = sys.argv[1]
        return file
    else:
        sys.exit("Not a python file")

def count_lines(user_file):


    try:

        count = 0
        with open(user_file) as file:
            for line in file:
                if not (line.strip().startswith("#") or line.strip() == ""):
                    count += 1
                else:
                    continue

            print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")




if __name__ == "__main__":
    main()