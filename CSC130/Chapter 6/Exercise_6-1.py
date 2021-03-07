names = []
for i in range(3):
    names.append(input('Enter name #{}: '.format(i+1)).strip())

file_handler = open('names.txt', 'w')
for name in names:
    file_handler.write(name + '\n')
file_handler.close()
