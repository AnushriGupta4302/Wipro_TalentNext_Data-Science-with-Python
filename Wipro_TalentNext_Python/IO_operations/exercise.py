#1 Write a program to read the entire content from a txt file and display it to the user.

file_name = input("Enter the name of the text file (with .txt extension): ")
with open(file_name, 'r') as file:
    content = file.read()
print(content)


#2 Write a program to read first in lines from a txt file. Get n as user input

file_name = input("Enter the file name (with .txt extension): ")
n = int(input("Enter the number of lines to read: "))
with open(file_name, 'r') as file:
    for i in range(n):
        line = file.readline()
        if not line: 
            break
        print(line.strip()) 


#3 Write a program to accept input from user and append it to a txt file.

file_name = input("Enter the file name (with .txt extension): ")
user_input = input("Enter the text to append to the file: ")
with open(file_name, 'a') as file:
    file.write(user_input + '\n')
print(file_name)


#4 Write a program to read contents from a txt file line by line and store each line into a list.

file_name = input("Enter the file name (with .txt extension): ")
with open(file_name, 'r') as file:
    lines_list = [line.strip() for line in file]  
print(lines_list)


#5 Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it

file_name = input("Enter the file name (with .txt extension): ")
with open(file_name, 'r') as file:
    content = file.read()              # Read entire content
    words = content.split()            # Split content into words
    longest_word = max(words, key=len) # Find the longest word by length
print(longest_word)


#6 Write a program to count the frequency of a user entered word in a txt file

file_name = input("Enter the file name (with .txt extension): ")
search_word = input("Enter the word to count: ").strip().lower()
with open(file_name, 'r') as file:
    content = file.read().lower()        
    words = content.split()              
    count = words.count(search_word)     
print(f"The word '{search_word}' appears {count} times in the file.")