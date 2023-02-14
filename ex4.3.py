def byfive():
    sum = 0
    for i in range(0, 105, 5):
        sum = sum + i
    print(sum)

def byfivewhile():
    sum = 0
    while sum < 1050:
        sum += 5
    print(sum)

byfive()