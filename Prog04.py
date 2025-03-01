#Prog04: Create a program that ask user to input 2 numbers input 2 numbers. Print the product of the two numbers.

class Style: #Colors/Style
    LIGHTCYAN = "\033[96m"
    RESET = '\033[0m'

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(Style.LIGHTCYAN + f"The product of {num1} and {num2} is {num1 * num2}." + Style.RESET)