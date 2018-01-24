# Project Euler
# Alex Johnson
# Problem 1: Multiples of 3 and 5

import time

start = time.time()
print(sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0))
elapsed = (time.time() - start) * 1000
print("Computed in {:.5g}ms".format(elapsed))
