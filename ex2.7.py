import math

def euros_to_bills():
    euros = int(input("Please give euros: "))
    if euros < 5:
        print("This is not enough for a single bill!")
    else:
        