def main():

    user_input = input("Input: ")
    shorten(user_input)


def shorten(word):

    vowels = ["a", "e", "i" , "o", "u"]

    for letter in word:
        if letter.lower() in vowels:
            continue
        else:
            print(letter, end="")

    print()

main()

