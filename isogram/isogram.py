import re


def is_isogram(string: str):
    string = re.sub(r'[^a-zA-Z]', '', string).lower()
    return len(string) == len(set(string))
