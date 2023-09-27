usinp=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ",)

usinp=usinp.lower().strip()

if usinp=='42' or usinp=='forty-two' or usinp=='forty two':
    print('Yes')
else:
    print('No')