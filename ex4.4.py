import random

def dicethrows():
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    n5 = 0
    n6 = 0

    for i in range(100):
        result = random.randint(1, 6)

        if result == 1:
            n1 += 1
        elif result == 2:
            n2 += 1
        elif result == 3:
            n3 += 1
        elif result == 4:
            n4 += 1
        elif result == 5:
            n5 += 1
        else:
            n6 += 1

    print(n1, n2, n3, n4, n5, n6)

dicethrows()