print("Name:Raushan kumar\nCRN:2221139\nURN:2203751")
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original List:", my_list)
# Count function: Count occurrences of a specific element
count_of_5 = my_list.count(5)
length=len(my_list)
print("length of my_list is:", length)
print("Count of 5:", count_of_5)
# Index function: Find the index of the first occurrence of a specific element
index_of_9 = my_list.index(9)
print("Index of 2:", index_of_9)
# Index function: Find the index of the first occurrence of a  element in between sub list
index_of_2 = my_list.index(2,4,8)
print("Index of 2:", index_of_2)
# Reverse function: Reverse the elements of the list 
my_list.reverse()
print("Reversed List:", my_list)
# Sort function: Sort the elements of the list in ascending order
my_list.sort()
print("Sorted List:", my_list)
# Sort function: Sort the elements of the list in decending order
my_list.sort(reverse=True)
print("Sorted List:", my_list)
# Min function: Find the minimum element in the list
min_element = min(my_list)
print("Minimum Element:", min_element)
# Max function: Find the maximum element in the list
max_element = max(my_list)
print("Maximum Element:", max_element)
