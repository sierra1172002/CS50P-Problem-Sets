import csv, sys
from tabulate import tabulate

def main():

    create_table(get_file_name())

#A function to get the correct file name.
def get_file_name():

#Check for valid number of command line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-lin arguments.")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-lin arguments.")

#Check if the correct file format is entered.
    elif sys.argv[1][-4:] == ".csv" and len(sys.argv) == 2:
        file = sys.argv[1]
        return file

#If not a csv file, exit with a prompt.
    else:
        sys.exit("Not a CSV file")



#A fucntion to create table from a '.csv' file.
def create_table(csv_file):

    #Store the rows from the .csv file as lists.
    table = []

    #open the csv file and add rows to the table.
    try:
        with open(csv_file) as content:
            reader = csv.reader(content)
            for row in reader:
                table.append(row)

    #Prompt if a non-existent filename is provided.
    except FileNotFoundError:
        sys.exit("File does not exist")

    #Once the table is created, display the contents in the dersired format.
    print(table)
    # print(tabulate(table[1:], headers = table[0], tablefmt = 'grid'))

if __name__ == "__main__":
    main()


