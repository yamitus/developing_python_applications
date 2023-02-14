def factorial():
    number = int(input("Please give a number: "))
    factorial = 1

    if number >= 1:
        for i in range(1, number + 1):
            factorial = factorial * i

    print("Factorial of", number, "is:", factorial)

factorial()