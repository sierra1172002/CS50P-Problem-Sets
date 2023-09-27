usinp=input('Expression: ').strip()

x, y, z=usinp.split(" ")

num1=float(x)
num2=float(z)

if y=='+':
    print(f"{(num1+num2):.1f}")
elif y=='-':
    print(f"{(num1-num2):.1f}")
elif y=='/':
    print(f"{(num1/num2):.1f}")
elif y=='*':
    print(f"{(num1*num2):.1f}")



