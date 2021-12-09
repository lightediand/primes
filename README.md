Two squares is a program that writes prime numbers under a given number n ∈ ℕ as the sum of two squares.

The program generates a list of p = a + b for each prime and creates a text file. Some primes may have more than one sum. 

The values for a and b are either:
1) a square, s = { n² | n ∈ ℕ }
2) a surd square, which is the square of a multiple of a surd, that is, 
   
   ss = { (n√p)² | n ∈ ℕ, p ∈ ℙ }, or equivalently, 
   
   ss = { n²p | n ∈ ℕ, p ∈ ℙ }.

With this information, we have factorised the prime numbers and can write the factors using complex numbers containing our surds √p.

For example, the program outputs 7 = 3 + 4, 

and from this we can go on to say that 7 =(√3 + 2i)(√3 -2i). 

These factors will fall in an extension of the ring ℤ, such as ℤ [ i, √p ].
