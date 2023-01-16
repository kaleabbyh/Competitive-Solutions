
def sum_of_multiples(limit, multiples):

    # return sum(set([i*j for i in multiples if i != 0 for j in range(1, int((limit-1)/i)+1)]))
    m = []
    for i in multiples:
        if i != 0:
            for j in range(1, int((limit-1)/i)+1):
                m.append(i*j)
    return sum(set(m))
