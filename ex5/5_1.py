import random

def random_array():
    my_list = []
    sum = 0
    for i in range(30):
        x = random.randint(0, 100)
        my_list.append(x)
    
    for i in range(len(my_list)):
        sum += my_list[i]
    print(sum)
    avg = sum / len(my_list)
    print(avg)

def find_max():
    my_list = []
    for i in range(30):
        x = random.randint(0, 100)
        my_list.append(x)
    print(my_list)
    maxval = max(my_list)
    print(maxval)

def find_val():
    my_list = []
    for i in range(30):
        x = random.randint(0, 100)
        my_list.append(x)
    
    found = 22
    foundval = False
    for i in range(len(my_list)):
        if my_list[i] == found:
            foundval = True
            print(my_list)
            print("Found value at position", i + 1)
            break
    if not foundval:
        print("Value not found!")

def sum_of_2():
    list1 = []
    list2 = []
    sum1 = 0
    sum2 = 0
    for i in range(20):
        x = random.randint(0, 100)
        list1.append(x)
    for i in range(20):
        x = random.randint(0, 100)
        list2.append(x)

    for i in range(len(list1)):
        sum1 += list1[i]
        sum2 += list2[i]
    totalsum = sum1 + sum2
    print(totalsum)

def lottorow():
    my_list = []
    for i in range(7):
        x = random.randint(0, 100)
        my_list.append(x)

eng_span = ["treaty", "patto"], ["truck", "camion"], ["trust", "trust"], ["value", "valore"], ["volunteer", "volontario"]

print(eng_span)