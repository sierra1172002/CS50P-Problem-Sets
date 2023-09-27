import csv
import sys


def main():

    check_file_name()
    create_csv(sys.argv[1], sys.argv[2])




#A function to get the correct file name.
def check_file_name():

    #Check for valid number of command line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-lin arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-lin arguments.")

    #Check if the correct file format is entered.
    elif sys.argv[1][-4:] == ".csv" and sys.argv[2][-4:] == ".csv" and len(sys.argv) == 3:
        return True

    #If not a csv file, exit with a prompt.
    else:
        sys.exit("Not a CSV file")




def create_csv(csv_file_1, csv_file_2):


    #open the csv file and add rows to the table.
    try:
        content = open(csv_file_1, "r")
        table = csv.DictReader(content)

    #Prompt if a non-existent filename is provided.
    except FileNotFoundError:
        sys.exit("Could not read file")

    #creating the new csv file using the data from lists in table variable
    updated = open(csv_file_2, "w")
    writer = csv.DictWriter(updated, ["first", "last", "house"])
    writer.writeheader()

    for row in table:
        last, first = row["name"].split(",")
        writer.writerow({"first": first.strip(),
                            "last": last,
                            "house": row["house"]})



if __name__ == "__main__":
    main()