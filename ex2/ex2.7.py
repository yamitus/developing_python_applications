def convert_to_bills(amount):
    bills = [500, 200, 100, 50, 20, 10, 5]
    result = {}
    for bill in bills:
        result[bill] = amount // bill
        amount = amount % bill
    return result

euros = int(input("Please give euros (round down to closest five): "))
bills = convert_to_bills(euros)
print(euros, "is in bills:", bills)