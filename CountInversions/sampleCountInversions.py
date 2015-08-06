__author__ = 'mcapizzi'

import random
import countInversions as c

print("generating random list to run countInversions on")
list = [random.randint(0, 15) for r in range(10)]         #ten digits

print("running countInversions")
c.countInversions(list, len(list))