# coin_flip_streaks.py

import random

numberofStreaks = 0
head_or_tails = []
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    if random.randint(0,1) == 0:
        head_or_tails.append('H')
    else: head_or_tails.append('T')
    # Code that checks if there is a streak of 6 'heads' or 'tails' in a row.
    # TODO
print(head_or_tails[:50])



print('Chance of streak: %s%%' % (numberofStreaks / 100))

