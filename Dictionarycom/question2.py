#create a dictionary that map each number from 1 to 5 to it factorial

import math
factorials = {x: math.factorial(x) for x in range(1, 6)}
print(factorials)