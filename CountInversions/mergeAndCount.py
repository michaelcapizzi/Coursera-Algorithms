__author__ = 'mcapizzi'

def mergeAndCount(a, b):
    c = []

    i = 0
    j = 0
    cCount = 0

    for k in range(len(a) + len(b)):
        if len(a) <= i and j <= len(b):            #if k is greater than a but not b
            c.append(b[j])
            j += 1
        elif len(b) <= j and i <= len(a):          #if k is greater than b but not a
            c.append(a[i])
            i += 1
        elif len(a) > i and len(b) > j:
            if a[i] >= b[j]:                        #handles duplicates
                c.append(b[j])
                j += 1
            elif b[j] > a[i]:
                c.append(a[i])
                i += 1
                cCount += len(a) - i

    return c, cCount
