"""Functions which helps the locomotive engineer to keep track of the train."""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*args):
    return list(args)


# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    a, b, c, *d = each_wagons_id
    return [c, *missing_wagons, *d, a, b]

# TODO: define the 'add_missing_stops()' function


def add_missing_stops(dicts, **kwargs):
    b = list(kwargs.values())
    return {**dicts, **{'stops': b}}


# TODO: define the 'extend_route_information()' function
def extend_route_information(route: dict, more_route_information: dict):
    b = {**route, **more_route_information}

    return b


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):

    return list(map(list, zip(*wagons_rows)))
