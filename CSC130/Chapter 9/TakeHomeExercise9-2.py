"""
(1) Create an empty set object my_set1.

(2) Add integer 1 into my_set1, using the add(argument) method.

(3) Add strings 'a', 'b', 'ab', '1', into my_set1, using the update(argument) method.

(4) Delete 'ab' from my_set1, using the remove(argument) method.

(5) Delete 'c' from my_set1, using the discard(argument) method.

(6) Create another set object my_set2, by calling set function with string 'abb1ab' as argument.

(7) Print out the updated set my_set1 and the set my_set2.

(8) Determine if my_set2 is a subset of my_set1, using the issubset(argument) method or the <= operator.

(9) Print out the union (using the union(argument) method or the | operator) and the intersection of the two sets
(using the intersection(argument) method or the & operator).
"""

my_set1 = set()
my_set1.add(1)
my_set1.update(['a','b','ab','1'])
my_set1.remove('ab')
my_set1.discard('c')
my_set2 = set('abb1ab')

print('my_set1:', my_set1)
print('my_set2:', my_set2)
print('Is my_set2 a subset of my_set1', my_set2.issubset(my_set1))
print('Union:', my_set2.union(my_set1))
print('Intersection:', my_set2.intersection(my_set1))
