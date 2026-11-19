#Number input function
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number")


#Welcome message
print("Welcome to the Mathex-Calculator!")


#Main program loop
while True:
    user_choice = input(
        "\nTo exit the calculator, enter E. To continue, enter C: "
    ).strip().upper()

    if user_choice == "E":
        print("You have exited the calculator. Goodbye!")
        break
    elif user_choice == "C":
        print("\nWelcome to the Mathex-Calculator!")

#Number input
        num1 = get_number("Enter your first number: ")
        num2 = get_number("Enter your second number: ")

#Operator selection
        valid_operators = ["+", "-", "*", "/", "//", "%", "**"]

        while True:
            operator = input("""Please select an operator:

    +    Addition
    -    Subtraction
    *    Multiplication
    /    Division
    //   Floor Division
    %    Modulus
    **   Power

Your choice: """).strip()

#Operator validation
            if operator in valid_operators:
                break
            else:
                print("Invalid operator! Please select a valid operator")

#Division by zero prevention
        while operator in ["/", "//", "%"] and num2 == 0:
            print("Operation by zero is not allowed. Please enter another number")
            num2 = get_number("Enter your second number: ")

#Mathe operations
        try:
            #Addition
            if operator == "+":
                result = num1 + num2

            #Subtraction
            elif operator == "-":
                result = num1 - num2

            #Multiplication
            elif operator == "*":
                result = num1 * num2

            #Division
            elif operator == "/":
                result = num1 / num2

            #Floor Division
            elif operator == "//":
                result = num1 // num2

            #Modulus
            elif operator == "%":
                result = num1 % num2

            #Power
            elif operator == "**":
                result = num1 ** num2

            #Display Result
            print("Result:", result)

        except ZeroDivisionError:
            print("Zero division is not allowed")

        except OverflowError:
            print("The result is too large to calculate")

#Invalid menu selection
    else:
        print("Invalid choice! Please enter E to exit or C to continue")