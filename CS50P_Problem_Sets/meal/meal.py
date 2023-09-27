def main():
    ans=input("What time is it? ").strip()
    t=convert(ans)

    if 7 <= t < 8:
        print('breakfast time')
    elif 12 <= t <=13:
        print('lunch time')
    elif 18 <= t <=19:
        print('dinner time')
    else:
        return



def convert(time):
    hrs, y=time.split(":")
    mins=float(y)/60
    return float(hrs)+mins

if __name__=="__main__":
    main()

