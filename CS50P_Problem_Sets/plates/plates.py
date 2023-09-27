def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Validation for all vanity license plates
def is_valid(s):

#Validate the length, first two characters are alphabets, others are alphabets or number.
#(The boundaries of the codes should be changeable while keeping the same code)
    if 7 > len(s) > 1 and s[0:2].isalpha() and s.isalnum():

        n = 2

        while n <= len(s):

            if n == len(s): #Make sure the function returns True value at the end.
                return True

            else:
                char = s[n]
                n=n+1
                if char.isalpha() and s[n-2].isalpha():
                    continue
                elif char.isnumeric() and char != "0" and s[n-2].isalpha():
                    continue
                elif char.isnumeric() and s[n-2].isnumeric():
                    continue
                else:
                    break   #Break if false no return required from function as 'None' wil be considered 'False' in main().

main()

