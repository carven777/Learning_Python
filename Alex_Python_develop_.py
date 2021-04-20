def fibanachi(x):
    if x==1:
        return 0
    if x == 2:
        return 1
    return fibanachi(x-1) + fibanachi(x-2)
print(fibanachi(10))


def poilindrom(p):
    if len(p) <= 1:
        return 'Yes'
    if p[0] != p[-1]:
        return 'No'
    return poilindrom(p[1:-1])
print(poilindrom('I22RIRIRIR2I'))

