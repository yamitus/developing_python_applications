def pyramid():
    number = int(input("Give the amount of rows: "))
    letter = "m"

    for i in range(number):
        print(letter * i)

pyramid()