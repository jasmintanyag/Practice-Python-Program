#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

class Style: #Color
    LIGHTMAGENTA = "\033[95m"
    RESET = '\033[0m'

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(Style.LIGHTMAGENTA + f"The bigger number is {max(num1, num2)}" + Style.RESET)