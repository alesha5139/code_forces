def test(d):
    seen = []
    inverted = {}
    for i in d:
        if d[i] in seen:
            pass
        else:
            if d[i] in inverted:
                del inverted[d[i]]
                seen.append(d[i])
            else:
                inverted[d[i]] = i

    return inverted
print(test({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3}))