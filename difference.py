from prime_sieve import prime_sieve

# getting a prime list from our function

n = 10
prime_list = prime_sieve(n)

with open("difference.txt","w") as f:

    for prime in prime_list:
        for j in range(len(prime_list)-1):
            for k in range(j, len(prime_list)):
                if prime_list[k] - prime_list[j] == prime:
                    f.write("{} = {} - {} \n".format(prime, prime_list[k], prime_list[j]))
