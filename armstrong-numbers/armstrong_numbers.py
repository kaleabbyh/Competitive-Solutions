def is_armstrong_number(number):
    number = str(number)
    return sum(int(i)**(len(number)) for i in number) == int(number)
