from random import randint
import sys

def main():

    while True:

        try:
            user_level = int(input("Level: "))
            if user_level < 1:
                continue
            else:
                break

        except ValueError:
            continue

    our_num = randint(1, user_level)

    while True:

        try:
            user_guess = int(input("Guess: "))
            if user_level > user_guess > 0:
                if user_guess < our_num:
                    print("Too small!")
                elif user_guess > our_num:
                    print("Too large!")
                elif user_guess == our_num :
                    sys.exit("Just right!")
            else:
                continue

        except ValueError:
            continue

if __name__ == '__main__':
    main()
