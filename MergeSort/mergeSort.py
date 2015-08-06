__author__ = 'mcapizzi'


import halfing as h
import merge as m

def mergeSort(z):
    print("splitting ", z)
    if len(z) <= 1:             #the absence of this was the problem!
        return z                #the absence of this was the problem!
    elif len(z) > 1:
        l, r = h.halfing(z)
        l = mergeSort(l)
        r = mergeSort(r)
        c = m.merge(l, r)
        return c


