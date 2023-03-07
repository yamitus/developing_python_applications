def return_factorial():
    number = int(input("Please give number to calculate: "))
    fact = 1

    for i in range(1, number + 1):
        fact = fact * i
    
    print(fact)

return_factorial()