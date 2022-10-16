#!/usr/bin/env python3

def prime_sieve(n: int):
    primes = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if (primes[p] == True):
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    return [x for x, is_prime in enumerate(primes) if is_prime]



n = 100
prime_list = prime_sieve(n)

# defining squares

square = [x*x for x in range(1,n)]

# defining surd squares

surd_square = []

for prime in prime_list:
    for x in range(1,n):
        surd_square.append(prime*x*x)

# combining the squares and surd squares into one list

squares = square + surd_square
squares.sort()

# writing the primes as the sum of two squares

f = open("primes.txt","w")

for prime in prime_list:
    for j in range (len(squares)-1):
        for k in range (j, len(squares)):
            if squares[j] + squares[k] == prime:
                f.write("{} = {} + {} \n".format(prime, squares[j], squares[k]))

f.close()
