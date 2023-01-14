"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS
                                  )


def clean_ingredients(dish_name, dish_ingredients):

    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    return f'{drink_name} Cocktail' if (set(drink_ingredients) & set(ALCOHOLS)) else f'{drink_name} Mocktail'


def categorize_dish(dish_name, dish_ingredients):
    a = {'VEGAN': VEGAN, 'VEGETARIAN': VEGETARIAN,
         'PALEO': PALEO, 'KETO': KETO, 'OMNIVORE': OMNIVORE}

    for i, j in a.items():
        if set(dish_ingredients).issubset(j):
            return f'{dish_name}: {i}'


def tag_special_ingredients(dish: tuple):
    dish = list(dish)
    dish[1] = (set(dish[1]) & set(SPECIAL_INGREDIENTS))

    return (tuple(dish))


def compile_ingredients(dishes):
    m = []
    for i in dishes:
        m.extend(list(i))
    return set(m)


def separate_appetizers(dishes: list, appetizers: list) -> list:

    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: list[set], intersection: set) -> set:

    singletons = (dish - intersection for dish in dishes)

    return set.union(*singletons)
