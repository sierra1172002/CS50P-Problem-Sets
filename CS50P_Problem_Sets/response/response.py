from validator_collection import is_email




def main():

    ask_val_email()




def ask_val_email():

    if (is_email(input("What is you email address? "))) == True:
        print("Valid")
    else:
        print("Invalid")




if __name__ == '__main__':
    main()