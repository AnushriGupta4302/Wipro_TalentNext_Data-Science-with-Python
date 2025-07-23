#1 Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("The result of division is:", result)


#2 Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

except ValueError:
    print("Error: Please enter a valid integer.")


#3 Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.

try:
    filename = input("Enter the file name to open: ")

    with open(filename, 'r') as file:
        contents = file.read()
        print("\nFile contents in title case:\n")
        print(contents.title())

except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: Could not read the file.")
except Exception as e:
    print("An unexpected error occurred:", e)


#4 Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message

numbers = [5, -3, 12, -8, 0, 7, -1, 9, -6, 4]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]

    if value > 0:
        print(f"The number at index {index} is positive.")
    elif value < 0:
        print(f"The number at index {index} is negative.")
    else:
        print(f"The number at index {index} is zero.")

except IndexError:
    print("Error: Index out of range. Please enter a number between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer index.")
except Exception as e:
    print("An unexpected error occurred:", e)