# setting the range

n = 100

# defining primes

# this works by generating a set of all the numbers 2 up to n
# the loop finds all the products xy within this range
# these are the composite numbers
# which are then discarded from the set to leave only primes

prime_list = set(range(2,n))

for x in range(2,n):
    for y in range(x,n):
        prime_list.discard(x*y)

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
