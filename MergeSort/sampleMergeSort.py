__author__ = 'mcapizzi'

import random
import mergeSort as m

print("generating random list to run mergeSort on")
list = [random.randint(0, 10000000) for r in range(10000000)]         #ten million digits

print("running mergeSort")
m.mergeSort(list)
