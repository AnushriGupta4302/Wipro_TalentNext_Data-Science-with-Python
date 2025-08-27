#1 Write a program to print the 4th element from first and 4th element from last in a tuple.

t = (10, 20, 30, 40, 50, 60, 70, 80)
fourth_from_start = t[3]
fourth_from_end = t[-4]
print("4th element from start:", fourth_from_start)
print("4th element from end:", fourth_from_end)


#2 Write a program to check whether an element exists in a tuple or not.

t = (10, 20, 30, 40, 50)
element = int(input("Enter the element to search: "))
if element in t:
    print("Yes")
else:
    print("No")


#3 Write a program to convert a list into a tuple.

lst = [10, 20, 30, 40, 50]
t_lst = tuple(lst)
print(t_lst)


#4 Write a program to find the index of an item in a tuple

my_tuple = (5, 10, 15, 20, 25, 30)
item = int(input("Enter the item to find its index: "))
if item in my_tuple:
    index = my_tuple.index(item)
    print("index is ",index)
else:
    print("item not found in the tuple.")


#5 Write a program to replace last value of tuples in a list to 100.
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
modified_list = [t[:-1] + (100,) for t in sample_list]
print(modified_list)


