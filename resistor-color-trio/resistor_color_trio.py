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


def label(colors: list):

    colors = [color.lower() for color in colors]

    a = dic.index(colors[0])
    b = dic.index(colors[1])
    c = dic.index(colors[2])

    result = (a * 10 + b) * 10 ** c
    rs = (a * 10 + b) * 10 ** (c % 3)

    if c >= 3:
        return str(rs) + " kiloohms"
    elif result % 1000 == 0:
        return str(result//1000)+" kiloohms"
    return str(result) + " ohms"
