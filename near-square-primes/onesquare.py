# setting the range

n = 100

# defining primes
# see comments on two squares for explanation

prime_list = set(range(2,n))

for x in range(2,n):
    for y in range(x,n):
        primes.discard(x*y)

# defining squares

square = [x*x for x in range(1,n)]

# writing the primes as the sum of one square plus one

f = open("nearsquareprimes.txt","w") 

for prime in prime_list:
    for j in range (len(square)-1):
            if square[j] + 1 == prime:
                f.write("{} = {} + {} \n".format(prime, square[j], 1))

f.close()
