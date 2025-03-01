#Prog06: Create a user program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

class Style: #Colors/Style
    LIGHTCYAN = "\033[96m"
    RESET = '\033[0m'

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(Style.LIGHTCYAN + f"{num1} raise to {num2} is {num1 ** num2}." + Style.RESET)