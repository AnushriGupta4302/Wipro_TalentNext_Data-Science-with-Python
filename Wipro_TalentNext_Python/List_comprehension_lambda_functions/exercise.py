#1 Write a LC program to create an output dictionary which contains only the odd numbers that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values
nums = [1, 2, 3, 4, 5, 6, 7]
output = {n: n**3 for n in nums if n % 2 != 0}
print(output)

#2 Make a dictionary of the 26 english alphabets mapping each with the corresponding integer
alphabet_dict = {chr(i): i - 96 for i in range(97, 123)}
print(alphabet_dict)

#3 cubes every number in the given list list_1 = [1,2,3,4,5,6,7,8,9]
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubes = [n**3 for n in list_1]
print(cubes)