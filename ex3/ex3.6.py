import random
import heapq

def findBiggest():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)

    my_list = [a, b, c]
    biggest = max(my_list)
    result = my_list.index(biggest)
    if result == 0:
        print("A is biggest.")
    elif result == 1:
        print("B is biggest.")
    else:
        print("C is biggest.")

def max():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    my_list = [a, b, c]
    max_ = my_list[0]
    for item in my_list:
        if item > max_:
            max_ = item
    result = my_list.index(item)
    if result == 0:
        print("A is biggest.")
    elif result == 1:
        print("B is biggest.")
    else:
        print("C is biggest.")

def bigheap():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    my_list = [a, b, c]
    biggest = heapq.nlargest(1, my_list)
    result = my_list.index(biggest)
    if result == 0:
        print("A is biggest.")
    elif result == 1:
        print("B is biggest.")
    else:
        print("C is biggest.")

bigheap()