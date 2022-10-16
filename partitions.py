from prime_sieve import prime_sieve

# getting a prime list from our function

n = 10
prime_list = prime_sieve(n)

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

with open("primes.txt","w") as f:

    for prime in prime_list:
        for j in range (len(squares)-1):
            for k in range (j, len(squares)):
                if squares[j] + squares[k] == prime:
                    f.write("{} = {} + {} \n".format(prime, squares[j], squares[k


with open("nearsquareprimes.txt","w") as f:

    for prime in prime_list:
        for j in range (len(square)-1):
            if square[j] + 1 == prime:
                f.write("{} = {} + {} \n".format(prime, square[j], 1))

with open("difference.txt","w") as f:

    for prime in prime_list:
        for j in range(len(prime_list)-1):
            for k in range(j, len(prime_list)):
                if prime_list[k] - prime_list[j] == prime:
                    f.write("{} = {} - {} \n".format(prime, prime_list[k], prime_list[j]))
