__author__ = 'mcapizzi'

def halfing(z):

    half = int(len(z)/2)

    if len(z) % 2 == 0:
        a = z[0:half]
        b = z[half:]
    else:
        b = z[0:half+1]
        a = z[half+1:]

    return a, b

################################