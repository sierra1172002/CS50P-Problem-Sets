import sys, inflect

def adieu_peeps():

    p = inflect.engine()

    names = []

    while True:
        try:
            user_name = input("Name: ")
            names.append(user_name)
        except EOFError:
            if len(names) == 0:
                sys.exit("\nPlease enter one name atleast.")
            else:
                print(f"\nAdieu, adieu, to {p.join(names)}" )
                break


if __name__ == '__main__':
    adieu_peeps()