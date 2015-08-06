__author__ = 'mcapizzi'

import mergeAndCount as mc
from MergeSort.halfing import halfing as h

def countInversions(z, n):
    if len(z) == 1:
        return 0
    else:
        l, r = h.halfing(z)
        lSorted, lCount = countInversions(l, n)
        rSorted, rCount = countInversions(r, n)
        sMerged, sCount = mc.mergeAndCount(z, n)
        return lCount + rCount + sCount
