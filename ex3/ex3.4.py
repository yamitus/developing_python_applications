def daysInMonth():
    month = input("Please give the month: ")
    if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
        print("This month has 31 days.")
    elif month == "February":
        print("This month has 28 days.")
    else:
        print("This month has 30 days.")

daysInMonth()