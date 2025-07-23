#1 Write a program to count the number of upper and lower case letters in a String.

text = input("Enter a string: ")
upper_count = 0
lower_count = 0
for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)


#2 Write a program that will check whether a given String is Palindrome or not.

# Input string from user
text = input("Enter a string: ")
cleaned_text = text.lower()
if cleaned_text == cleaned_text[::-1]:
    print("palindrome")
else:
    print("not a palindrome")


#3 Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2. If input is "Wipro" then output should be "WiWiWiWiwi".

text = input("Enter a string (length >= 2): ")
first_two = text[:2]
n = len(text)
result = first_two * n
print("Output:", result)


#4 Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi"

text = input("Enter a string: ")
if text.startswith('x'):
    text = text[1:]
if text.endswith('x'):
    text = text[:-1]
print("Output:", text)


#5 Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 8 and the length of the string inclusive. For example if the inputs are "Wipro" and 3, then the output should be "propropro".

text = input("Enter a string: ")
n = int(input("Enter an integer n (8 <= n <= len(string)): "))
if n >= 8 and n <= len(text):
    last_n_chars = text[-n:]
    result = last_n_chars * n
    print("Output:", result)
else:
    print("Invalid input")