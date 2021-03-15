"""
Write a program that first creates a dictionary object phonebook with the following information (Name as the key; Phone Number as the value):

Name	Phone Number
Alice	1234
Bob	4567
Charlie	7890
Then, perform the following tasks to the dictionary:

(1) Use bracket [] based assignment to add the key-value pair ('David', 1357) into the dictionary,
    and change Bob's phone number to 2468. Print the updated dictionary.

(2) Use in or not in operator to decide whether the record with key 'Charlie' exists.
    If so (implemented with decision structure ), use the del statement to remove the record of Charlie. Print the updated dictionary.

(3) Use get(key, default) method to retrieve and print Bob's phone number.
    If the record does not exist, "Not Found!" is printed out instead.

(4) Use pop(key, default) method to retrieve and pop Alice's phone number.
    If the record exists, print Alice's phone number and the updated dictionary; otherwise, print "Not Found!".

(5) Use keys() method to retrieve and print all names in the dictionary.
"""

phonebook = {'Alice': 1234, 'Bob': 4567, 'Charlie': 7890}

print('Original:', phonebook)
phonebook['David'] = 1357
phonebook['Bob'] = 2468
print('After Assignment:', phonebook)

if 'Charlie' in phonebook:
    del phonebook['Charlie']
print('After Deletion:', phonebook)

if 'Bob' in phonebook:
    print("Bob's phone number is", phonebook.get('Bob'))
else:
    print('Not Found!')

if 'Alice' in phonebook:
    print("Alice's phone number is", phonebook.pop('Alice'))
    print('After pop:', phonebook)
else:
    print('Not Found!')

print('Names in the dictionary: ', phonebook.keys())
