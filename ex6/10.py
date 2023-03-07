import random

def from_array():
    number = int(input("Please give the number to search for: "))
    the_list = []
    for i in range(10):
        a = random.randint(1, 10)
        the_list.append(a)
    
    for i in the_list:
        if i == number:
            print("Found number at position", the_list.index(i))
            break

from_array()