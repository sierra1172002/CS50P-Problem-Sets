from random import randint

def main():

    no_rep = []

    lvl = get_level()
    score = 0
    i=0
    while i < 10:

        x, y = generate_integer(lvl)
        if str(x) + str(y) not in no_rep and str(y) + str(x) not in no_rep:

            z = x + y
            no_rep.append(str(x)+str(y))
            no_rep.append(str(y)+str(x))
            i += 1
            error = 0
            while True:
                print(f"{x} + {y} = ", end="")
                user_ans = input().strip()

                if user_ans == str(z):
                    score += 1
                    break
                elif user_ans != str(z) and error < 2:
                    error += 1
                    print("EEE")
                    continue
                else:
                    print("EEE")
                    print(f"{x} + {y} = {z}")
                    break

        else:
            continue


    print(f"Score: {score}")

def get_level():

    while True:

        try:
            user_level = int(input("Level: ").strip())

            if 0 < user_level < 4:
                return user_level
            else:
                continue

        except ValueError:
            continue


def generate_integer(level):


    if level == 1:
        x = randint(0,9)
        y = randint(0,9)
    elif level == 2:
        x = randint(10,99)
        y = randint(10,99)
    else:
        x = randint(100,999)
        y = randint(100,999)
    return (x, y)




if __name__ == '__main__':
     main()




