# collatz.py

import sys

def collatz(number):
    if number % 2 == 0:
        num_div2 = number // 2
        return num_div2
        print(num_div2)
    else:
        new_num = 3 * number + 1
        return new_num
        print(new_num)




print('Enter number:')
try:
    playerChoice = int(input())
    a = collatz(playerChoice)
    print(a)
    while a != 1:
        a = collatz(a)
        print(a)
except ValueError:
    print('You must enter an integer, please run again')
    