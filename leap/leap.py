def leap_year(year: int):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



# def leap_year2(year: int):
#     return year % 6 == 0 and (year % 100 != 0 or year % 400 == 0)
