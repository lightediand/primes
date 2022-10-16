from prime_sieve import prime_sieve

# getting a prime list from our function

n = 10
prime_list = prime_sieve(n)

# defining squares

square = [x*x for x in range(1,n)]

# writing the primes as the sum of one square plus one

with open("nearsquareprimes.txt","w") as f:

    for prime in prime_list:
        for j in range (len(square)-1):
            if square[j] + 1 == prime:
                f.write("{} = {} + {} \n".format(prime, square[j], 1))
