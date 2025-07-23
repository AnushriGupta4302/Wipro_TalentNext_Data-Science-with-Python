#1 write a program to create a list of 5 integers and display the list items
my_list = [10, 25, 40, 55, 70]
for item in my_list:
    print(item)


#2 write a program to append a new item to the end of the list 
my_list = ["a", "b", "c"]
print(my_list)
new_item = "d"
my_list.append(new_item)
print(my_list)


#3 write a program to reverse the order of the items in the list
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)


#4 write a program to print the number of occurrences of specified element in list
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 3, 7, 3]
count = 0
for val in a: 
	if val == 3:
		count += 1
print(count)


#5 write a program to append the items of list1 to list2 in the front 
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
new_list = list1 + list2
print(new_list)


#6 write a program to insert a new item before the second element in an existing list
lst = ["b","c","d"]
lst.insert(1,"a")
print(lst)

#7 write a program to remove the item from a specified index in a list
my_list = ["a", "b", "c", "d"]
print(my_list)
index_to_remove = 2
removed_item = my_list.pop(index_to_remove)
#print(removed_item)
print(my_list)


#8 write a program to remove the first occurence of a specified element in a list
my_list = [30,10, 20, 30, 40, 30, 50]
element_to_remove = 30
if element_to_remove in my_list:
    r_list = my_list.remove(element_to_remove)
    print(my_list)
else:
    print("Element not found.")