import math

def expansion(numerator, denominator, base,lim):

    arr = []
    counter = 0
    while(counter < lim):

        arr.insert(counter, math.floor(base*numerator/denominator))
        numerator = base*numerator
        numerator = numerator - arr[counter]*denominator
        counter += 1

    return arr

lim = 80
num1 = 4
denom1 = 7
base1 = 3
arr = expansion(num1,denom1, base1,lim)

print('a = (', end = '')
for num in arr:
    print(num, end=', ')

print(')', end='')
