dic = ['black',
       'brown',
       'red',
       'orange',
       'yellow',
       'green',
       'blue',
       'violet',
       'grey',
       'white']


def value(colors: list):
    a, b, *c = colors
    return int(str(dic.index(a))+str(dic.index(b)))
