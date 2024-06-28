# The instructions are to "write a program that creates a dictionary", so it feels like cheating if i simply create it like normal.
# room_numbers_dict = {"CSC101": 3004,
#                      "CSC102": 4501,
#                      "CSC103": 6755,
#                      "NET110": 1244,
#                      "COM241": 1411}

# instructors_dict = {"CSC101": "Haynes",
#                     "CSC102": "Alvarado",
#                     "CSC103": "Rich",
#                     "NET110": "Burke",
#                     "COM241": "Lee"}

# start_times_dict = {'CSC101': '8:00 a.m.',
#                     'CSC102': '9:00 a.m.',
#                     'CSC103': '10:00 a.m.',
#                     'NET110': '11:00 a.m.',
#                     'COM241': '1:00 p.m.'}

courses = ["CSC101", "CSC102", "CSC103", "NET110", "COM241"]
room_numbers = [3004, 4501, 6755, 1244, 1411]
instructors = ["Haynes", "Alvarado", "Rich", "Burke", "Lee"]
start_times = ["8:00 a.m.", "9:00 a.m.", "10:00 a.m.", "11:00 a.m.", "1:00 p.m."]

room_numbers_dict = dict(zip(courses, room_numbers))
instructors_dict = dict(zip(courses, instructors))
start_times_dict = dict(zip(courses, start_times))

while True:
    user_input = str(input("\nPlease enter a course number (or Q to quit): ")).upper()
    if user_input == "Q":
        print("Have a great day!")
        break
    elif user_input not in room_numbers_dict.keys():
        print(f"I'm sorry, but '{user_input}' is not a valid course.")
    else:
        print(f"Course Number {user_input} is lead by Professor {instructors_dict[user_input]} and begins at {start_times_dict[user_input]} in room #{room_numbers_dict[user_input]}.")

