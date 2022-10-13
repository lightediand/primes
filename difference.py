# setting the range

n = 100

# defining primes
# see comments on two squares for explanation

prime_list = set(range(2,n))

for x in range(2,n):
    for y in range(x,n):
        primes.discard(x*y)

f = open("difference.txt","w") 

for prime in prime_list:
    for j in range(len(prime_list)-1):
        for k in range(j, len(prime_list)):
            if prime_list[k] - prime_list[j] == prime:
                f.write("{} = {} - {} \n".format(prime, prime_list[k], prime_list[j]))

f.close()

