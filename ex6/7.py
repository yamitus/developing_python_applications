import random

def biggest():
    the_list = []
    for i in range(5):
        a = random.randint(0, 100)
        the_list.append(a)
    
    print("The values are:", the_list)
    max_val = max(the_list)
    print("Max value is:", max_val)

biggest()