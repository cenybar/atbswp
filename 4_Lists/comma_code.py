# comma_code.py

def comma_code(list):
    if list == []:
        raise ValueError('List can\'t be empty')
    newList = ', '.join(list[:-1])
    finalString = newList + ", and " + list[-1]
    print(finalString)
    