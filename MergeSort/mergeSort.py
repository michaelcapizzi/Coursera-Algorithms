__author__ = 'mcapizzi'


import halfing as h
import merge as m

def mergeSort(z):
    print("splitting ", z)
    if len(z) > 1:
        l, r = h.halfing(z)
        print("running mergeSort on left ", l)
        mergeSort(l)
        print("running mergeSort on right ", r)
        mergeSort(r)
        print("merging", l, r)
        c = m.merge(l, r)
        print("merged", c)



