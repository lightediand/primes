from prime_sieve import prime_sieve

natural_number  = input("Please specify a natural number for the range: ") 

# the above returns the input as a string
# so we must convert it to an integer

n = int(natural_number)

# getting a prime list from our function

print("Starting sieve...")
prime_list = prime_sieve(n)
print("Primes obtained!")

# defining squares
print("Getting the squares...")
square = [x*x for x in range(1,n)]
print("Squares acquired!")

# defining surd squares
print("Now getting the surd squares which are totally a thing...")
surd_square = []

for prime in prime_list:
    for x in range(1,n):
        surd_square.append(prime*x*x)

print("We got em!")

# combining the squares and surd squares into one list

squares_incl_surd_squares = square + surd_square
squares_incl_surd_squares.sort()

print("Writing primes as the sum of two squares...")

with open("primes.txt","w") as f:

    for prime in prime_list:
        for j in range (len(squares_incl_surd_squares)-1):
            for k in range (j, len(squares_incl_surd_squares)):
                if squares_incl_surd_squares[j] + squares_incl_surd_squares[k] == prime:
                    f.write("{} = {} + {} \n".format(prime, squares_incl_surd_squares[j], squares_incl_surd_squares[k]))

print("Done!")

print("Writing primes as the sum of a square and 1...")

with open("nearsquareprimes.txt","w") as f:

    for prime in prime_list:
        for j in range (len(square)-1):
            if square[j] + 1 == prime:
                f.write("{} = {} + {} \n".format(prime, square[j], 1))

print("Done!")

print("Writing primes as the difference of a prime and 2...")

with open("twinprimes.txt","w") as f:

    for prime in prime_list:
            for j in range(len(prime_list)):
                if prime_list[j] - 2 == prime:
                    f.write("{} = {} - {} \n".format(prime_list[j], prime, 2))
                    
print("All done!")

