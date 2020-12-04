# addto.py

from inventory import displayInventory 


def addToInventory(inventory, addedItems):
    for element in addedItems:
        if element not in inventory.keys():
            inventory.setdefault(element,1)
        else: inventory[element] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

