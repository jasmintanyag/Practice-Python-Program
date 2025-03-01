#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point.

class Style: #Colors/Style
    LIGHTMAGENTA = "\033[95m"
    RED = "\033[31m"
    BOLD = "\033[1m"
    RESET = '\033[0m'
    
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
if num2 == 0:
    print(Style.RED + Style.BOLD + "Cannot divide by zero." + Style.RESET)
else:
    print(Style.LIGHTMAGENTA + f"The quotient of {num1} and {num2} is {num1 / num2}." + Style.RESET)