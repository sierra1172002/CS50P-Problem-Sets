def main ():
    req_amt()


def req_amt():

    amt_due=50
    accept_denomination = [25, 10, 5]
    while amt_due > 0:
        print(f"Amount Due: {amt_due}")
        insert_coin = int(input("Insert Coin: "))
        if insert_coin in accept_denomination:
            amt_due -= insert_coin
        if amt_due <= 0:
            print(f"Change Owed: {amt_due * -1}")

main()