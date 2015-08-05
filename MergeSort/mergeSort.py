__author__ = 'mcapizzi'


import halfing as h
import merge as m

def mergeSort(z):
    print("splitting ", z)
    if len(z) > 1:
        a, b = h.halfing(z)
        print("running mergeSort on ", a)
        mergeSort(a)
        print("running mergeSort on ", b)
        mergeSort(b)
        print("merging", a, b)
        c = m.merge(a, b)
        print("merged", c)





