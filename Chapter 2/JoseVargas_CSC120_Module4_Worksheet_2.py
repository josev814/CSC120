def capitalize_words(string, separator):
    str_list = string.split(separator)
    cap_list = []
    for word in str_list:
       cap_list.append(word.capitalize())
    return ' '.join(cap_list)


student_info = {}  # dictionary
student_info['name'] = input('What is your name? ')  # string
student_info['city'] = input('What city are you from? ')  # string
student_info['state'] = input('What state are you from? ')  # string
student_info['major'] = input('What is your major? ')  # string
student_info['classification'] = input('What is your classification? ')  # string
student_info['high_school_gpa'] = float(input('What was your High School GPA? '))  # float
student_info['enrolled_courses'] = []  # list

for i in range(3):  # prompt user with these questions 3 times
    option = 'first'
    if i == 1:
        option = 'second'
    elif i == 2:
        option = 'third'
    student_info['enrolled_courses'].append({})
    student_info['enrolled_courses'][i]['name'] = input('What is the {} class name you are enrolled in? '.format(option))  # string
    student_info['enrolled_courses'][i]['code'] = input('What is the course code for {} (ex: CSC)? '.format(
        student_info['enrolled_courses'][i]['name']
    ))  # string
    student_info['enrolled_courses'][i]['number'] = int(input('What is the course number for {} (ex: 120)? '.format(
        student_info['enrolled_courses'][i]['name']
    )))  # int
    student_info['enrolled_courses'][i]['credits'] = int(input('How many credits do you receive for completing the course? (ex: 3)? '))  # int

for dict_key in student_info:
    if '_' in dict_key:
        ucwords_dict_key = capitalize_words(dict_key, '_')
    else:
        ucwords_dict_key = dict_key.capitalize()
    if dict_key == 'enrolled_courses':
        print('{}:'.format(ucwords_dict_key))
        for _class in student_info['enrolled_courses']:
            print('{}{} {}, Credits: {}'.format(
                _class['code'],
                _class['number'],
                _class['name'],
                _class['credits']
            ))
    elif dict_key == 'city':
        print('City and State of Origin: {}, {}'.format(
            student_info[dict_key],student_info['state']
        ))
    elif dict_key == 'state':
        pass # ignoring state, since city references that value
    else:
        print('{}: {}'.format(ucwords_dict_key, student_info[dict_key]))