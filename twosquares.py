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
