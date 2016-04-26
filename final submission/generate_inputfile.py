import sys
import random

with open("input.txt", 'w') as f:
    sys.stdout = f

    i=0
    for i in range(100):
        print random.randrange(1,10**12,100)
