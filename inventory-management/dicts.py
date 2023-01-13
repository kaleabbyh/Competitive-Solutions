"""Functions to keep track and alter inventory."""


def create_inventory(items: list):
    return {i: items.count(i) for i in set(items)}


def add_items(inventory, items):

    for i in items:
        inventory[i] = inventory.get(i, 0) + 1
    return inventory


def decrement_items(inventory, items):

    for item in items:
        inventory[item] = max(inventory[item] - 1, 0)
    return inventory


def remove_item(inventory: dict, item):
    if item in inventory:
        del inventory[item]

    return inventory


def list_inventory(inventory: dict):
    # m = []
    # for i in inventory:
    #     if inventory[i] > 0:
    #         m.append((i, inventory[i]))

    return [(m, n) for m, n in inventory.items() if n > 0]
