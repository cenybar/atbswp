# inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(dictionary):
    print('Inventory:')
    itemTotal = 0
    for key, value in dictionary.items():
        print(value, key)
        itemTotal += value
    print('Total number of tiems: ' + str(itemTotal))

#displayInventory(stuff)