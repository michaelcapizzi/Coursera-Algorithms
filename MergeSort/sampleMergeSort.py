__author__ = 'mcapizzi'

import random
import mergeSort as m

print("generating random list to run mergeSort on")
list = [random.randint(0, 15) for r in range(15)]         #ten million digits

print("running mergeSort")
sortedList = m.mergeSort(list)
print(sortedList)

