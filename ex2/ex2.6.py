import math

def seconds_to_hours():
    seconds = int(input("Please give seconds: "))
    if seconds < 3600:
        minutes = seconds / 60
        new_seconds = (minutes % 1 * 100) / 100
        final_seconds = round(new_seconds * 60)
        final_minutes = math.floor(minutes % 100)
        print(seconds, "seconds is", final_minutes, "minutes and", final_seconds, "seconds.")
    elif seconds % 3600 == 0:
        hours = round(seconds / 3600)
        print(seconds, "seconds is", hours, "hours.")
    else:
        hours = seconds / 3600
        final_hours = math.floor(hours % 100000000)
        minutes = (hours % 1 * 100) / 100
        new_minutes = (minutes * 60)
        final_minutes = math.floor(new_minutes)
        new_seconds = (new_minutes % 1 * 100) / 100
        final_seconds = round(new_seconds * 60)
        print(seconds, "seconds is", final_hours, "hours,", final_minutes, "minutes and", final_seconds, "seconds.")

seconds_to_hours()