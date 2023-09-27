from pyfiglet import Figlet
import sys
from random import choice


def con_to_figlet():

    list_font = Figlet().getFonts()

    try:

        if len(sys.argv) == 1:
            font_style = choice(list_font)

        elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in list_font:
            font_style = sys.argv[2]

        f=Figlet(font=font_style)

        user_input = input("Input: ")

        print("Output: \n",f.renderText(user_input))

    except:
        sys.exit("Invalid Usage")


if __name__ == '__main__':
    con_to_figlet()

