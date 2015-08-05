__author__ = 'mcapizzi'


import halfing as h
import merge as m

def runMergeSort(z):
    sortedA = []
    sortedB = []
    mergeSort(z)

def mergeSort(z):
    if len(z) > 1:
        print("halfing ", z)
        a, b = h.halfing(z)
        print("running mergeSort on ", a)
        mergeSort(a)
        print("running mergeSort on ", b)
        mergeSort(b)
        print("merging", a, b)
        c = m.merge(a, b)
        print("merged", c)
    else:
        a, b = h.halfing(z)
        c = m.merge(a, b)
        print("merge", c)



