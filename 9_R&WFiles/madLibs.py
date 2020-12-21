# madLibs.py

from pathlib import Path
import os
import sys

ADJECTIVE = input('Enter an adjective: ')
NOUN = input('Enter an noun: ')
VERB = input('Enter an verb: ')
NOUN2 = input('Enter an adjective: ') 

def madLibs():
    text = f"The {ADJECTIVE} panda walked to the {NOUN} and then {VERB}. A nearby {NOUN2} was unaffected by these events."
    print(text)
    sys.stdout = open('madLibs.txt', 'w')
    print(text)
    sys.stdout.close()


madLibs()
