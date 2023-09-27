#Ask user for a camelCase
def main():
    camel_Case = input("camelCase: ")
#Print snake_case withoiut adding a line to allow the conversion to printed in line
    print("snake_case: ", end="")
    camel_to_snake(camel_Case)

#Creat a function to convert from camel to snake case
def camel_to_snake(c_case):

    #Recreate the camelCase letter by letter
    for letter in c_case:
        #Add a "_" before a letter in Upper Case.
        if letter.isupper():
            print("_"+letter.lower(), end="")
        else:
            print(letter, end="")
    #Add a line after the for loop
    print()

main()
