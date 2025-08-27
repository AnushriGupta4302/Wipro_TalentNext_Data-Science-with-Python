#1 Write a program to remove a given item from the set.

my_set = {10, 20, 30, 40, 50}
item = int(input("Enter the item to remove from the set: "))
if item in my_set:
    my_set.remove(item)  
else:
    print("item not found ")
print( my_set)


#2 Write a program to create an intersection of sets.

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
intersection_set = set1.intersection(set2)
#print("Set 1:", set1)
#print("Set 2:", set2)
print(intersection_set)


#3 Write a program to create an union of sets.

set1 = {10, 20, 30}
set2 = {30, 40, 50}
union_set = set1.union(set2)
#print("Set 1:", set1)
#print("Set 2:", set2)
print(union_set)


#4 Write a program to find the maximum and minimum value in a set.

my_set = {15, 42, 7, 89, 23, 3}
max_value = max(my_set)
min_value = min(my_set)
print("Maximum:", max_value)
print("Minimum ", min_value)
