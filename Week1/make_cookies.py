def add_and_subtract(user_numbers):
    try:
        # attempt to add the numbers together
        addition = user_numbers[0] + user_numbers[1]
    except Exception as e:
        addition = f"A addition error occurred.  Num1: {user_numbers[0]} | Num2: {user_numbers[1]} | Error: {e}"
    try:
        # Attempt to subtract the numbers
        subtraction = user_numbers[0] - user_numbers[1]
    except Exception as e:
        subtraction = f"A subtraction error occurred.  Num1: {user_numbers[0]} | Num2: {user_numbers[1]} | Error: {e}"
    # return the results of the above math attempts
    return addition, subtraction


def multiply_and_divide(user_numbers):
    try:
        # Attempt to multiply the numbers
        multiplication = user_numbers[0] * user_numbers[1]
    except Exception as e:
        multiplication = f"A multiplication error occurred.  Num1: {user_numbers[0]} | Num2: {user_numbers[1]} | Error: {e}"
    try:
        # Attempt to divide the numbers
        division = user_numbers[0] / user_numbers[1]
    except Exception as e:
        division = f"A division error occurred.  Num1: {user_numbers[0]} | Num2: {user_numbers[1]} | Error: {e}"
    # return the results of the above math attempts
    return multiplication, division


def get_user_input():
    try:
        # Ensure the user input is a valid number by converting to a float vlaue
        user_input = float(input("Enter a number: "))
    except:
        # If it is not a real number - call this function again and try again
        print("Invalid response.  Please enter a valid number.")
        user_input = get_user_input()
    # Return the valid/real number
    return user_input


# Create an empty list to store the users numbers
user_numbers = []
while len(user_numbers) < 2:
    # get the user feedback and store it into the list - the function checks if the user input is valid
    number = get_user_input()
    user_numbers.append(number)

# call math functions and return results
add_numbers, subtract_numbers = add_and_subtract(user_numbers)
multiply_numbers, diviside_numbers = multiply_and_divide(user_numbers)

# Print output
print(f"\nAddition: {user_numbers[0]} + {user_numbers[1]} = {add_numbers}")
print(f"Subtraction: {user_numbers[0]} - {user_numbers[1]} = {subtract_numbers}")
print(f"Multiplication: {user_numbers[0]} * {user_numbers[1]} = {multiply_numbers}")
print(f"Division: {user_numbers[0]} / {user_numbers[1]} = {diviside_numbers}")
