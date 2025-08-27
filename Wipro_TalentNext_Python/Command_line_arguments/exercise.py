#1 Write a program to accept two numbers as command line arguments and display their sum.

import sys
if len(sys.argv) != 3:
    print("Usage: python sum_args.py <num1> <num2>")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum:", num1 + num2)


#2 Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

import sys
if len(sys.argv) < 2:
    print("Usage: python welcome.py <welcome message>")
else:
    file_name = sys.argv[0]                      
    message = ' '.join(sys.argv[1:])             
    print("File Name:", file_name)
    print("Welcome Message:", message)


#3 Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

import sys
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
if len(sys.argv) != 11:
    print("Usage: python sum_primes.py <10 numbers>")
else:
    numbers = [int(arg) for arg in sys.argv[1:]]
    prime_sum = sum(num for num in numbers if is_prime(num))
    print(prime_sum)


