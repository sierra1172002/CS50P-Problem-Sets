def main():
    usinp=input()

    print(convert(usinp))


def convert(s):
    return s.replace(":)","🙂").replace(":(","🙁")

main()