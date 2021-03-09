"""
Write a Python program that can perform the following operations on list:

(1) Create a list that contains the elements below:

     45, 67, 34, 89, 31, 52

(2) Insert number 76 to the middle of the list (between 34 and 89) with the insert(index, item) method. Print the updated list.

(3) Sort the list in ascending order with the sort() method. Print the updated list.

(4) Remove the number 89 from the list with the remove(item) method. Print the updated list.

(5) Reverse the order of elements in the list with the reverse() method. Print the updated list.

(6) Delete the first element of the list with the del statement. print the updated list.

(7) Find the minimum element and the maximum element of the list, using the min function and max function. Print these two elements.
"""
mylist = [45, 67, 34, 89, 31, 52]
print('Original list:', mylist)

mylist.insert(mylist.index(89), 76)
print('List after insertion:', mylist)

mylist.sort()
print('List after sorting:', mylist)

mylist.remove(89)
print('List after removing:', mylist)

mylist.reverse()
print('List after reversing:', mylist)

del mylist[0]
print('List after deletion:', mylist)

print('Minimum element: {} Maximum element: {}'.format(min(mylist), max(mylist)))
