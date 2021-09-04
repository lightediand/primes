import numpy as np

# setting the range
r = 10

# defining the square
square = [x*x for x in range(1,r)]

# defining primes
p = []

for x in range(r):
    if x>1:
        for i in range(2, x):
            if (x % i) ==0:
                break
        else:
            p.append(x)

# defining surd squares
surd_square = []

for prime in p:
    for x in range(1,r):
        surd_square.append(prime*x*x)

# combining the squares and surd squares
L = square + surd_square
