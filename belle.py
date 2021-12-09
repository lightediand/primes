# setting the range

n = 1000000

# defining primes

p = []

for x in range(n):
    if x>1:
        for i in range(2, x):
            if (x % i) ==0:
                break
        else:
            p.append(x)

# defining squares

square = [x*x for x in range(1,n)]

L = square
L.sort()

# writing the primes as the sum of squares and surd squares 

f = open("nearsquareprimes.txt","w") 

for prime in p:
    for number in range (len(L)-1):
            if L[number] + 1 == prime:
                f.write("{} = {} + {} \n".format(prime, L[number], 1))

f.close()
