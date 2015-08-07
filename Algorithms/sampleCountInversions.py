__author__ = 'mcapizzi'

import random
import CountInversions.countInversions as c

print("generating random list to run countInversions on")
outputList = [random.randint(0, 1000) for r in range(1000)]         #ten digits

print("running countInversions")
print(c.countInversions(outputList))
