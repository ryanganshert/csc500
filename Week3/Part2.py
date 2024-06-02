"""
Part 2:
Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you
set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the
above problem. Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
Your program should output what the time will be on a 24-hour clock when the alarm goes off.
"""

current_hour = 0
values = []
while len(values) < 2:
    current_hour = input("What is the current hour? (Type 'q' to quit): ")
    try:
        values.append(round(float(current_hour), 0))
    except:
        try:
            if str(current_hour)[0].upper() == "Q":
                break
            else:
                print("Please enter a valid time in whole hours.")
        except:
            print("Please enter a valid time in whole hours.")

    hours_to_alarm = input(f"You'd like to set an alarm for how many hours from {current_hour}:00? ")
    try:
        values.append(round(float(hours_to_alarm), 0))
    except:
        print("Please enter a valid whole hours for desired hours.")

days = int((values[0] + values[1]) / 24)
alarm_hour = int((values[0] + values[1]) % 24)

if days < 1:
    print(f"Your alarm will go off at {alarm_hour}:00.")
elif days == 1:
    print(f"Your alarm will go off tomorrow {alarm_hour}:00.")
else:
    print(f"Your alarm will go off in {days} days at {alarm_hour}:00.")
print("Have a great day!!  :-)")