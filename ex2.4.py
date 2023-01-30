def bmi_calc():
    height = int(input("Please enter height in cm: "))
    weight = int(input("Please enter weight in kg: "))
    new_height = height / 100
    squared_height = round(new_height ** 2, 2)
    bmi = weight / squared_height
    if bmi < 18.5:
        print("You are under weight!")
    elif 18.5 <= bmi < 25:
        print("You are normal weight!")
    elif 25 <= bmi < 30:
        print("You are over weight!")
    elif 30 <= bmi < 35:
        print("You have class 1 obesity!")
    elif 35 <= bmi < 40:
        print("You have class 2 obesity!")
    else:
        print("You have extreme obesity!")

bmi_calc()