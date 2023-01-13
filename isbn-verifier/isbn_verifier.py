def is_valid(isbn: str):
    isbn = isbn.replace('-', '')
    isbn = list(isbn)
    if len(isbn) != 0:
        isbn[-1] = '10' if isbn[-1].lower() == 'x' else isbn[-1]
    sum = 0
    if len(isbn) != 10:
        return False
    elif "".join(isbn).isnumeric():
        for i in range(len(isbn)):
            sum += (len(isbn)-i)*int(isbn[i])
        return sum % 11 == 0
    else:
        return False
