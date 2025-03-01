#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.54

class Style: #Colors/Style
    LIGHTCYAN = "\033[96m"
    RESET = '\033[0m'

odd_counter = 0
for i in range(10):
    number = float(input(f"Enter a number ({i+1}): "))
    if number %2 != 0:
        odd_counter += 1
print(Style.LIGHTCYAN + f"The number of odd numbers is: {odd_counter}" +Style.RESET)