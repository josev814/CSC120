file_handler = open('flowers.txt', 'r')
line = file_handler.readline()
while line:
    print(line.rstrip('\n'))
    line = file_handler.readline()
file_handler.close()
