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

# defining squares

square = [x*x for x in range(1,n)]

# writing the primes as the sum of one square plus one

f = open("nearsquareprimes.txt","w") 

for prime in prime_list:
    for j in range (len(square)-1):
            if square[j] + 1 == prime:
                f.write("{} = {} + {} \n".format(prime, square[j], 1))

f.close()
