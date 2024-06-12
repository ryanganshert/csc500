"""Part 2: The CSU Global Bookstore has a book club that awards points to its students based on the number of
books purchased each month. The points are awarded as follows:
    If a customer purchases 0 books, they earn 0 points.
    If a customer purchases 2 books, they earn 5 points.
    If a customer purchases 4 books, they earn 15 points.
    If a customer purchases 6 books, they earn 30 points.
    If a customer purchases 8 or more books, they earn 60 points.
Write a program that asks the user to enter the number of books that they have purchased this month and then
display the number of points awarded."""

points_dict = {0: 0,
               2: 5,
               4: 15,
               6: 30,
               8: 60}

valid_response = False
while not valid_response:
    try:
        books_purchased = float(input("How many books have you purchased this month? "))
        if books_purchased % 1 == 0:
            valid_response = True
        else:
            print("Invalid entry!  You cannot purchase a part of a book.  Please try again.")
    except:
        print("Invalid entry!  Please enter a whole number.")

points = 0
for k, v in points_dict.items():
    if books_purchased >= k:
        points = v

if books_purchased == 0:
    print("Zero books purchased?  I hope you enjoyed the break.")
elif books_purchased < 4:
    print(f"Only {int(books_purchased)} books?  That's a pretty light load this month.")
elif books_purchased < 10:
    print(f"Nice! {int(books_purchased)} books this month.  Keep up the good work!")
elif books_purchased < 25:
    print(f"You're a rockstar! {int(books_purchased)} books this month.  That's amazing!")
else:
    print(f"You're messing with me, right?  There's no way you purchased {int(books_purchased)} books this month.")
