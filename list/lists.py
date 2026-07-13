lst1= [2,4,4,5,7]
lst2= [1,2,3,4,5]

first_el= lst1[0]
reverse_lst= lst1[::-1]
# to append an element to the list
lst1.append(10)

# to append elemet in specific index
lst1.insert(2, 3)

# to extend the list with another list
lst1.extend(lst2)
# to remove an element from the list
lst1.remove(4)
# to pop an element from the list
lst1.pop(3)
# to know index of an element in the list
index_of_5= lst1.index(5)
print("Index of 5 in lst1:", index_of_5)

# to know the count of an element in the list
count_of_4= lst1.count(4)
print("Count of 4 in lst1:", count_of_4)

#  len() function to know the length of the list
length_of_lst1= len(lst1)
print("Length of lst1:", length_of_lst1)

# sum() function to get the sum of elements in the list
sum_of_lst1= sum(lst1)
print("Sum of elements in lst1:", sum_of_lst1)

# clear() function to remove all elements from the list
# lst1.clear()

# sort() function to sort the list in ascending order
lst1.sort()
print("Sorted lst1:", lst1)


# print(lst1)
# print(first_el)
# print(reverse_lst)
   
