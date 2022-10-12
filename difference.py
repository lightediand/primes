# setting the range

n = 100

# defining primes

prime_list = []

for x in range(n):
    if x>1:
        for i in range(2, x):
            if (x % i) ==0:
                break
        else:
            prime_list.append(x)


f = open("difference.txt","w") 

for prime in prime_list:
    for j in range(len(prime_list)-1):
        for k in range(j, len(prime_list)):
            if prime_list[k] - prime_list[j] == prime:
                f.write("{} = {} - {} \n".format(prime, prime_list[k], prime_list[j]))

f.close()

