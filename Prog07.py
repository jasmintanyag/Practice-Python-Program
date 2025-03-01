#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

class Style: #Color
    LIGHTMAGENTA = "\033[95m"
    RESET = '\033[0m'

total = 0
for i in range(10):
    number = float(input(f"Enter a number ({i+1}): "))
    total += number
print(Style.LIGHTMAGENTA + f"The sum of all number is {total}" + Style.RESET)