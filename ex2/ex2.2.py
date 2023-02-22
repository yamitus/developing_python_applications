def resistance_calc():
    u = int(input("Please give voltage: "))
    i = int(input("Please give current: "))
    r = u / i
    print("Resistance is:", r)

resistance_calc()