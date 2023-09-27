def main():
    get_fuel_lvl()


def get_fuel_lvl():

    while True:

        user_input=input("Fraction: ").split("/")

        try:
            fuel_lvl= float (int(user_input[0]) / int(user_input[1]))
            if 1/100 < fuel_lvl < 99/100:
                print(int(round(fuel_lvl*100,0)),"%", sep="")
            elif 0 <= fuel_lvl <= 1/100:
                print("E")
            elif 1 >= fuel_lvl >= 99/100:
                print("F")
            elif fuel_lvl < 0 or fuel_lvl > 1:
                continue

        except (ValueError, ZeroDivisionError):
            continue
        break

main()




