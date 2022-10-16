#!/usr/bin/env python3

def prime_sieve(n: int):
    primes = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if (primes[p] == True):
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    return [x for x, is_prime in enumerate(primes) if is_prime][2:]
