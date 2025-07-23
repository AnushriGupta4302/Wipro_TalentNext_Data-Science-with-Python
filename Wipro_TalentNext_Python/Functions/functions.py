#1 Write a function to return the sum of all numbers in a list.
#Sample List: (8, 2, 3, 8, 7)
#Expected Output: 20

def sum_of_list(numbers):
    return sum(numbers)
sample_list = (8, 2, 3, 8, 7)
result = sum_of_list(sample_list)
print(result)


#2 Write a function to return the reverse of a string.
#Sample String: "1234abcd"
#Expected Output "dcba4321"

def reverse_string(s):
    return s[::-1]
sample = "1234abcd"
result = reverse_string(sample)
print(result)


#3 Write a function to calculate and return the factorial of a number (a non-negative)

def factorial(n):
    if n < 0:
        return "Factorial is not defined"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
num = int(input("Enter a non-negative number: "))
print(factorial(num))


#4 Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("uppercase letters:", upper_count)
    print("lowercase letters:", lower_count)
text = input("Enter a string: ")
count_case(text)


#5 Write a function to print the even numbers from a given list. List is passed to the function as an argument.
#Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result [2, 4, 6, 8]

def print_even_num(numbers):
    even_num = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_num)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_num(lst)


#6 Write a function that takes a number as a parameter and checks whether the number is prime or not.

def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print("prime number")
else:
    print("not a prime number")


