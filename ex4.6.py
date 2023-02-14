def equation():
    y = 0
    x = -5
    while True:
        y = 3 * x ** 3 - 4 * x ** 2 + 9 * x + 5
        if y > -0.001 and y < 0.001:
            break
        x += 0.0001
    print(x)
    print(y)

equation()