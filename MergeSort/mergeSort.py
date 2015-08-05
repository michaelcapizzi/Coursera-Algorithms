__author__ = 'mcapizzi'


import halfing as h
import merge as m


def mergeSort(z):
    sortedArray = []
    if len(z) > 1:
        print("halfing ", z)
        a, b = h.halfing(z)
        print("recursion")
        mergeSort(a)
        mergeSort(b)
        print("merging", a, b)
        c = m.merge(a, b)
        print("merged", c)
        print("adding", c, "to sortedArray")
        for i in c:
        sortedArray.append(i)
    return sortedArray
