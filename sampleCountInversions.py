__author__ = 'mcapizzi'

import random
import CountInversions.countInversions as c

print("generating random list to run countInversions on")
outputList = [random.randint(0, 10) for r in range(4)]         #ten digits
#outputList = [8,3,0,4,6,9,2,8,10,5]

print("running countInversions")
print("original list: ", outputList)
print("# of inversions: ", c.countInversions(outputList))
