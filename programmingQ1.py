__author__ = 'mcapizzi'

import CountInversions.countInversions as c

f = open("/home/mcapizzi/Github/Coursera-Algorithms/IntegerArray.txt", "r")

inputList = [int(p) for p in f.readlines()]     #read in each line as an integer element in list

print(c.countInversions(inputList))

