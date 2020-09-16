print("""Where strexp is a string that will inserted to the end of the displayed output. 
What is displayed by the following program? """)
print("-"*50)
print('Hello,', end=' ')
print('My name is', end= ' ')
print('Peter Williams')
print('Hello,', end='**')
print('My name is', end= '**')
print('Peter William')

print("-"*50, "-"*50, "-"*50)
print("""Separator argument in a print function is used to separate other arguments when they are displayed. 
sep = strexp 
Where strexp is a string that is inserted between all other arguments in the print function.
What is displayed by the following program? """)
print("-"*50)
x = 9
y = 5
z = 13
print(x % y, z/y, x+y*z, x**2*y, sep='&')
print(x % y, z/y, x+y*z, x**2*y, sep='**')
print(x % y, z/y, x+y*z, x**2*y, sep='AAA')


print("-"*50, "-"*50, "-"*50)
print("""Escape characters are used to format a string output. 
\n  - newline 
\t – horizontal tab 
\’ – display single quote 
\’’ – display double quotes 
\\ -  display backslash 
What is displayed by the following program? """)

print("-"*50)
print('The student\'s name is Cynthia.\nShe graduated from\nFayetteville State University')
print('Item\tPrice')
print('Milk\t$2.50')
print('Cereal\t$3.95')

print("-"*50, "-"*50, "-"*50)
print("""The operator (+) can be used to concatenate two or more strings. 
What is displayed from the following program? """)

print("-"*50)
print('The price of box of cereal is $' + str(2.95))

print('When studying for chapter one\'s test' +

      ' I read a lot of materials both from the ' +

      'textbook and the Internet. ' +

      'I experienced some challenges with the Internet' +

      ' due to hurricane Florence')

print("-"*50, "-"*50, "-"*50)
print("""The format function is used to format output.
The format specifier is second argument in the format function and it is a special string used to specify how the output should be formatted. 
The general syntaxes are :
‘jw,.pt’ 
‘jw.pt’ 
‘jwt’ 
j is the either empty, > (right justified) or < (left justified, default) 
w is the number of spaces reserved for the output 
p is the precision (or the number of decimal places). Note that the number is rounded up. 
t is the data type of the number, f for float, d for integer, s for string 
The dot (.) is required only when you want to format numbers.  
What is displayed from the following program? """)
print("-"*50)
print(format('Item', '>10s'), format('Price', '>10s'))
print(format('Item', '<10s'), format('Price', '<10s'))
print(format(78398.828298182, '20,.4f'))
print(format(78398.828298182, '20.4f'))
print(format(78398.828298182, '20,.5f'))
print(format(78398.828298182, ',.6f'))
print(format(78398.828298182, ',.2f'))
print(format(9938847, ',d'))
print(format(.56345, '.1%'))
print(format(.56385, '.1%'))
