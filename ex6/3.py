import random

def sum_array():
    the_list = []
    for i in range(10):
        a = random.randint(1, 100)
        the_list.append(a)
    
    sums = 0
    for i in the_list:
        sums = sums + i
    
    print(sums)

sum_array()