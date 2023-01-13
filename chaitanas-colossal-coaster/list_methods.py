
def add_me_to_the_queue(express_queue: list, normal_queue: list, ticket_type: int, person_name: str):

    return express_queue+[person_name] if ticket_type == 1 else normal_queue+[person_name]


def find_my_friend(queue: list, friend_name: str):

    return queue.index(friend_name)


def add_me_with_my_friends(queue: list, index, person_name):

    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list, person_name):

    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list, person_name):

    return queue.count(person_name)


def remove_the_last_person(queue: list):
    return queue.pop()


def sorted_names(queue: list):

    queue.sort()
    return queue
