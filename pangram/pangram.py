import re


def is_pangram(sentence):
    noun1 = re.sub(r'[^a-zA-Z]', '', sentence).strip().lower()
    if len(set(noun1)) == 26:
        return True
    else:
        return False
