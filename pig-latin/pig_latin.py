

def check(text: str):
    if not text.startswith(('a', 'e', 'i', 'o', 'u')):
        if text[1:3] == 'qu':
            return f'{text[3:]}{text[0:3]}ay'
    if text.startswith(('xr', 'yt', 'a', 'e', 'i', 'o', 'u')):
        return f'{text}ay'
    if text.startswith('qu'):
        return f'{text[2:]}{text[:2] }ay'
    if set('aieou') - set(text) == set('aieou') and 'yt' not in text:
        return text[1:] + text[:1] + "ay"
    return check(text[1:] + text[0])


def translate(text):
    return ' '.join([check(word) for word in text.split(' ')])
