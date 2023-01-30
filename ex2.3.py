def time_to_travel():
    speed = int(input("Please give the average speed of the vehicle in km/h: "))
    distance = int(input("Please give distance to be travelled in kilometers: "))
    hours = (distance / speed)
    string_hours = str(hours)
    final_hours = string_hours[0]
    minutes = (hours % 1 * 100) / 100
    final_minutes = round(minutes * 60)
    if final_hours == '1':
        print("The journey takes approx.", final_hours, "hour and", final_minutes, "minutes.")
    else:
        print("The journey takes approx.", final_hours, "hours and", final_minutes, "minutes.")

time_to_travel()