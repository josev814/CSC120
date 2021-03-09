"""
Write a program which performs the following tasks

(1) define a list named num and initialize it with the following values:

10, 35, 60, 55, 50, 70, 15, 80, 90

(2) use the append(item) method to add element 65 to the end of the list. Print the appended list num.

(3) use the index(item) method to get the index number of element 35 and element 80. Print out the two index numbers.

(4) use the slicing expression to extract a slice/subsection of the list starting from the element 35 up to element 80 (80 included), using the index numbers obtained in the previous step. Print the extracted slice.

(5) use the in operator to detect if 65 is in the slice, print the result (True or False).

(6) insert number 25 into the list between element 60 and element 55, using the insert(index, item) method. Print the updated list num.

(7) sort the list in ascending order using the sort() method. Print the updated list num.
"""

num = [10, 35, 60, 55, 50, 70, 15, 80, 90]
print('The original list is', num)
num.append(65)
print('The appended list is', num)
ind1 = num.index(35)
ind2 = num.index(80)
print('The index numbers for 35 and 80 are {} and {}'.format(ind1, ind2))
sliced = num[ind1:ind2+1]
print('The extracted slice is {}'.format(sliced))
if 65 in sliced:
    print('If 65 is in the slice:', True)
else:
    print('If 65 is in the slice:', False)
num.insert(num.index(55), 25)
print('List after insertion', num)
num.sort()
print('List after sorting', num)
