print("""Write the following mathematical expressions in Python. Assume, x, y, z, a, b, c are variables. 
xy(z+a) + b3 
(x+y)(a+b+2)5 
X2y + ab3 """)

x, y, z, a, b, c = 11, 12, 13, 1, 2, 3
print(
    'Python code:',
    'print(x*y*(z+a)+b**3, x+y*((a+b+2)**5), (x**2)*y+a*(b**3))'
)
print('Answer:', x*y*(z+a)+b**3, (x+y)*(a+b+2)**5, (x**2)*y+a*(b**3))
print()
print("""Write a program that will prompt the user to enter the size of square with an inscribed circle. The program will calculate the area of the shaded region using the formula:  

area of shaded region = area of square – area of circle = s2 (1- p/4), p = 3.1414 """)

square_length = float(input('What is the length of the square? '))
area_of_square = square_length**2
area_of_circle = area_of_square*(1.0 - 3.1313/4)
area_of_shaded_region = area_of_square - area_of_circle
print('The shaded area of the square is {} '.format(area_of_shaded_region))

