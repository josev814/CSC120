print("Algorithm Workbench: #1 and #2 (page 103)", 'Write Python code that prompts the user to enter his or her height and assigns the user’s input to a variable named height')
height = input('What is your height? ')

print('-'*50, '-'*50, '-'*50)
print("Write Python code that prompts the user to enter his or her favorite color and assigns the user’s input to a variable named color ")
color = input('What is your favorite color? ')

print('-'*50, '-'*50, '-'*50)
print("""Answer following questions.  
Write a statement that will prompt the user to enter age (an integer)  and assign to the age.""")
age = int(input('What is your age? '))

print('-'*50, '-'*50, '-'*50)
print("""Write a statement that will prompt the user to enter major  (a string)  and assign to the major. """)
major = input('What is your major? ') 

print('-'*50, '-'*50, '-'*50)
print("""Write a statement that will prompt the user to enter CGPA  (a real)  and assign to the c_gpa. """)
c_gpa = float(input('What is your gpa? '))

print('-'*50, '-'*50, '-'*50)
print("""Write a statement that will prompt the user to enter classification  (a string)  and assign to the std_class. """)
std_class = input('What is your classification? ') 

print('-'*50, '-'*50, '-'*50)
print("""Write a statement that will prompt the user to enter  street name (a string )  and assign to the street_name. """)
street_name = input('What street do you live on? ')

print('-'*50, '-'*50, '-'*50)
print("""Write a statement that will prompt the user to enter street number  (an integer)  and assign to the street_no. """)
street_no = int(input('What is your street number? ')) 

print('-'*50, '-'*50, '-'*50)
print('Write a statement that will prompt the user to enter city (a string)  and assign to the city. ')
city = input('What city do you live in? ')

print('-'*50, '-'*50, '-'*50)
print('Write a statement that will prompt the user to enter state (a string)  and assign to the state. ')
state = input('What state do you live in? ')

print('-'*50, '-'*50, '-'*50)
print('Write a statement that will prompt the user to enter zip code (an integer)  and assign to the zip_code. ')
zip_code = int(input('What is your zip_code? ')) 

print('-'*50, '-'*50, '-'*50)
print('Write a statement that will prompt the user to enter a name (a string)  and assign to the name. ')
name = input('What is your name? ') 

print('-'*50, '-'*50, '-'*50)
print('Write statements that will display (variables will be replaced with what the user enters.)')

print("""Name = {}
Age = {}
Major = {}, Classification = {}, CGPA = {}
Street No = {}, Street Name = {}
City = {}, State = {}, Zip Code = {}""".format(  
    name, age, major, std_class, c_gpa, street_no, street_name,
    city, state, zip_code
))
