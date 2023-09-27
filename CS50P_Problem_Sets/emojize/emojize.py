import emoji
import sys

def main():

    convert_to_emojis()


def convert_to_emojis():

    try:
        user_input = input("Input: ")

        print("Output:",emoji.emojize(user_input))

    except:

        sys.exit()


main()