def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dol):
    return round(float(dol.replace("$","")),2)

def percent_to_float(per):
    per=(float(per.replace("%","")))/100
    return round(per,2)

main()