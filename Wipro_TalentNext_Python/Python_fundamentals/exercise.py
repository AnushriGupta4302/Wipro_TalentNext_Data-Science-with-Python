 # Q1. Write a program to check if a given number is Positive, Negative or Zero.
number = int(input("Enter a number"))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


#Q2. Write a program to check if a given number is odd or even.
n = int(input("Enter a digit"))
if (n%2 == 0):
    print("Even number")
else:
    print("Odd number")


#Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
def has_same_last_digit(num1, num2):
  return num1 % 10 == num2 % 10
print(f"Do 27 and 57 have the same last digit? {has_same_last_digit(27, 57)}")
print(f"Do 27 and 57 have the same last digit? {has_same_last_digit(12, 34)}")
print(f"Do 27 and 57 have the same last digit? {has_same_last_digit(10, 20)}")
print(f"Do 27 and 57 have the same last digit? {has_same_last_digit(5, 15)}")


#Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1,11):
  print(i,end='\t')


#Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(23,57):
  if(i%2==0):
    print(i)


#Q6. Write a program to check if a given number is prime or not.
num = int(input("Enter the number: "))
if(num==1):
  print("Not a Prime number")
else:
  for i in range(2,num//2):
    if(num%i==0):
      print("Not a Prime")
      break
  else:
    print("Prime number")


#Q7. Write a program to print prime numbers between 10 and 99.
for num in range(10,99):
  for i in range(2,num//2):
    if(num%i==0):
      break
  else:
    print(num)


#Q8. Write a program to print the sum of all the digits of a given number.
n = int(input("Enter the number: "))
s = 0
while(n!=0):
  digit = n%10
  s += digit
  n //= 10
print(s)


#Q9. Write a program to reverse a given number and print.
num = int(input("Enter number"))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(reversed_num)


#Q10. Write a program to find if the given number is palindrom or not.
numb = input("Enter the number: ")
reverse = ''
for i in range((len(numb)-1),-1,-1):
  reverse += numb[i]
if(numb == reverse):
  print('Palindrome')
else:
  print('Not Palindrome')