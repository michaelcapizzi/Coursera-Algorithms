__author__ = 'mcapizzi'

import random
import timeit
import mergeSort as m

print("generating random list to run mergeSort on")
list = [random.randint(0, 10000000) for r in range(10000000)]         #ten million digits

print("running mergeSort")
time = m.mergeSort(list)

print(list)
print("time to merge and sort: ", time)
