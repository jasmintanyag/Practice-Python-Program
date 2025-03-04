#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

class Style: #Colors/Style
    LIGHTCYAN = "\033[96m"
    RED = "\033[31m"
    BOLD = "\033[1m"
    RESET = '\033[0m'

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
if num1 == num2:
    print(Style.LIGHTCYAN + Style.BOLD + "Equal" + Style.RESET)
