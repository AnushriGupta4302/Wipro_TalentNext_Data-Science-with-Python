#1 Write a program to add a key and value to a dictionary.
#Sample Dictionary: {0:10, 1: 20}
#Expected Result: {0: 10, 1:20, 2:30}
d = {0:10, 1: 20}
d.update({2:30})
print(d)


#2 Write a program to concatenate the following dictionaries to create a new one.
#Sample Dictionary:dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 
#Expected Result: {1: 10, 2: 20, 3: 30, 4:40, 5: 50, 6: 60}
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
merge_dict = {}
for d in (dic1, dic2, dic3):
    merge_dict.update(d)
print(merge_dict)


#3 Write a program to check if a given key already exists in a dictionary.
n = input("Enter key for checking")
d = {'a': 1, 'b': 2, 'c': 3}
key = n
print(key in d)


#4 Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
d = {'a': 1, 'b': 2, 'c': 3, 'd':4}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key,value in d.items():
    print(f"{key}:{value}")


#5 Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
sq_dict = {}
for n in range(1,16):
    sq_dict[n] = n**2
print(sq_dict)


#6 Write a program to sum all the values in a dictionary, considering the values will be of int type
d = {'a': 1, 'b': 2, 'c': 3, 'd':4}
res = sum(d.values())
print(res)