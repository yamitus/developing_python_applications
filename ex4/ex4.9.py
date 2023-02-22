def exponent():
    base = float(input("Give base number: "))
    exp = int(input("Give exponent: "))

    for i in range(0, exp):
        print(base ** i)

exponent()