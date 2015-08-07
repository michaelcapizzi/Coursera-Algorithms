import mergeAndCount
from MergeSort import halfing
from MergeSort import mergeSort

__author__ = 'mcapizzi'


def countInversions(z):
    if len(z) == 1:
        return 0
    else:
        l, r = halfing.halfing(z)
        l = mergeSort.mergeSort(l)
        r = mergeSort.mergeSort(r)
        s, sCount = mergeAndCount.mergeAndCount(l, r)
        return sCount
