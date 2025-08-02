# Beginner Friendly Calculator

print("Welcome to My Calculator!")

# Ask the user for two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")


# Ask for the operation
operation = input("Choose + for addition, - for subtraction, * for multiplication, / for division: ")

# Do the math
if operation == "+":
    answer = num1 + num2
elif operation == "-":
    answer = num1 - num2
elif operation == "*":
    answer = num1 * num2
elif operation == "/":
    answer = num1 / num2
else:
    answer = "Sorry, that operation is not recognized."

# Show the result
print("Your Answer is:", answer)
# End of the calculator program