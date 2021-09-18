import numpy as np

# setting the range
n = 10

# defining the square
square = [x*x for x in range(1,n)]

# defining primes
p = []

for x in range(n):
    if x>1:
        for i in range(2, x):
            if (x % i) ==0:
                break
        else:
            p.append(x)

# defining surd squares
surd_square = []

for prime in p:
    for x in range(1,n):
        surd_square.append(prime*x*x)

# combining the squares and surd squares
L = square + surd_square

complex_factors = []

for prime in p:
    for number in range (len(L)-1):
        for value in range (number, len(L)):
            if L[number] + L[value] == prime:
              complex_factors.append((prime, L[number], L[value]))  

print(complex_factors)
