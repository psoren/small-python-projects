import time
import random
import matplotlib.pyplot as plt

num = 0
largest = ''
while not largest.isdigit():     
    print('Please enter the largest array you want to sort: ')
    largest = input()
    if largest.isdigit() and int(largest) > 0:
        num = int(largest)
        break       

alg = ''
while alg != 'T' and alg != 'B':
    print('Enter B for Bogosort or T for Timsort: ')
    alg = input()

def bogo(x):
    while x != sorted(x):
       random.shuffle(x)
    return x

times = {}
count = 1
while count <= num:
    start = time.time()
    x = random.sample(range(1, count*2), count)
    start = time.time()

    if alg == 'T':
        if count % 250 == 0:
            print('Timsort: ' + str(count))
        x.sort()
    if alg == 'B':
        print('Bogo: '+ str(count))
        x = bogo(x)

    times.update({count:time.time() - start})    
    count += 1
   
plt.bar(range(len(times)), times.values(), align='center')
plt.xticks(range(len(times)), times.keys())
plt.xlabel('Array Length', fontsize=18)
plt.ylabel('Time', fontsize=16)
plt.show()

