
def main():
    input = [0, 4, 100, 34,52,47, 47, 47, 1, 3, 5, 2, 57, 58, 24, 47, 22]
    input = [[i] for i in input]
    print mergeSort(input)

def mergeSort(input):
    r = []
    oddN = None
    if len(input) == 1:
        return input[0]
    indexes = [(a, a+1) for a in xrange(0, len(input), 2)]
    if len(indexes) > 1 and len(indexes) % 2:
        oddN = indexes.pop(-1)
    for i in indexes:
        a, b = i
        r.append(merge(input[a], input[b]))
    if oddN:
        r.append(merge(r.pop(-1), input[-1]))
    return mergeSort(r)


def merge(a, b, extra=None):
    res = []
    while len(a) or len(b):
        if not a:
            res.append(b.pop(0))
        elif not b:
            res.append(a.pop(0))
        elif a[0] > b[0]:
            res.append(b.pop(0))
        else:
            res.append(a.pop(0))
    return res

main()