from MergeSort.mergeSort import merge
from Utils import utils as u


__author__ = 'mcapizzi'

def mergeSortAndCount(z):            #fix this to include counts!  not counting left and right inversions
    if len(z) <= 1:
        return z
    elif len(z) > 1:
        l, r = u.halfing(z)
        l = mergeSortAndCount(l)
        r = mergeSortAndCount(r)
        c = merge(l, r)
        return c


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

################################

def countInversions(z):                     #doesn't work!  misses some inversions
    if len(z) == 1:
        return 0
    else:
        l, r = u.halfing(z)
        l = mergeSortAndCount(l)            #this needs a count
        r = mergeSortAndCount(r)            #this needs a count
        s, sCount = mergeAndCount(l, r)
        return sCount

