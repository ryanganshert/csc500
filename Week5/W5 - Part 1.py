"""Part 1: Write a program that uses nested loops to collect data and calculate the average rainfall over a
period of years. The program should first ask for the number of years. The outer loop will iterate once for
each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop
will ask the user for the inches of rainfall for that month. After all iterations, the program should display
the number of months, the total inches of rainfall, and the average rainfall per month for the entire period."""

months_dict = {1: "January",
               2: "February",
               3: "March",
               4: "April",
               5: "May",
               6: "June",
               7: "July",
               8: "August",
               9: "September",
               10: "October",
               11: "November",
               12: "December"}

years = 0
while years == 0:
    try:
        years = int(input("How many years would you like to provide data for? "))
    except:
        print("Invalid entry!  Please enter a whole number.")

rainfall = []
for y in range(years):
    for m in range(12):
        invalid_entry = True
        while invalid_entry:
            try:
                if y == years - 1:
                    rainfall_in_month = float(input(f"How much did in rain in {months_dict[m + 1]} last year? "))
                else:
                    rainfall_in_month = float(input(f"How much did in rain in {months_dict[m + 1]} {-y + years} years ago? "))

                if rainfall_in_month < 0:
                    print("Invalid entry!  Rainfall cannot be a negative value.")
                else:
                    rainfall.append(rainfall_in_month)
                    invalid_entry = False
            except:
                print("Invalid entry!  Please enter a real number.")

print(f"\nTotal months of data collected: {len(rainfall)}")
total_rainfall = 0
for r in rainfall:
    total_rainfall += r
print(f"Average monthly rainfall: {total_rainfall / len(rainfall):,.2f}")
print(f"Total rainfall for all {len(rainfall)} months: {total_rainfall:,.2f}")
