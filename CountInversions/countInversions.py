__author__ = 'mcapizzi'

# import sys
# sys.path.append("../MergeSort")

import mergeAndCount as mc
from MergeSort.halfing import halfing           #I'm getting an import error.  Why?


def countInversions(z, n):
    if len(z) == 1:
        return 0
    else:
        l, r = halfing(z)
        lSorted, lCount = countInversions(l, n)
        rSorted, rCount = countInversions(r, n)
        sMerged, sCount = mc.mergeAndCount(z, n)
        return lCount + rCount + sCount
