# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Error: Division by zero!")
# else:
#     print("No exceptions occurred.")
# finally:
#     print("Execution completed. Cleaning up resources...")



try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    # This runs if a ValueError occurs (e.g., input is not a number)
    print("That's not a valid number!")
except ZeroDivisionError:
    # This runs if a ZeroDivisionError occurs (e.g., division by zero)
    print("You can't divide by zero!")
finally:
    # This runs no matter what
    print("Finished trying to divide.")