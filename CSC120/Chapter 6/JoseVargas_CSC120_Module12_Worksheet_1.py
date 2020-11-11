"""
Professor: Daniel Okunbor
Student: Jose' Vargas
Class: CSC 120
Module: 12
Assignment: Worksheet
Date: 2020-11-10
"""

"""
Activity 
    Write a program that will prompt the user to enter 10 grocery items, their available quantities and unit prices. 
        Write these values to a file productRec.txt. Store values in separate lines. 
    Using the file in (1), calculate the value of each product (unit price * quantity), 
        store the product names and values in separate file productValues.txt. 
    Using the productValues.txt in (2), 
        calculate and display the overall total value (i.e., the sum of all product values). 
        Use 2 decimal places to total value
"""
PRODUCT_TABLE = r'productRec.txt'
PRODUCT_VALUE_TABLE = r'productValues.txt'
SEPARATOR = '\t'
COLUMNS = ('Item', 'Quantity', 'Unit Price')
VALUE_COLUMNS = ('Item', 'Price')
PRODUCT_LIMIT = 10


def get_product_input():
    product_name = input('Enter a product to add: ')
    qty = str(get_int_input('How many {}s are in stock? '.format(product_name)))
    unit_price = '{:.2f}'.format(get_float_input('What is the price per {}? '.format(product_name)))
    return [product_name, qty, unit_price]


def get_int_input(quest):
    valid_input = False
    while not valid_input:
        try:
            qty = int(input(quest))
            if qty < 0:
                raise ValueError
            valid_input = True
        except ValueError:
            print()
            print('ERROR: The quantity must be a positive integer', end='\n\n')
    return qty


def get_float_input(quest):
    valid_input = False
    while not valid_input:
        try:
            unit_price = float(input(quest))
            if unit_price < 0:
                raise ValueError
            valid_input = True
        except ValueError:
            print()
            print('ERROR: The price must be a positive float', end='\n\n')
    return unit_price


def activity_one():
    items = [SEPARATOR.join(COLUMNS) + '\n']
    for i in range(PRODUCT_LIMIT):
        item_info = get_product_input()
        items.append(SEPARATOR.join(item_info) + '\n')
    del item_info  # gc
    with open(PRODUCT_TABLE, 'w') as pth:
        pth.writelines(items)
    del items  # gc


def get_items_from_file(file):
    items = []
    with open(file, 'r') as fh:
        header = True
        for line in fh:
            if header:
                header = False
                continue
            items.append(line.rstrip('\n').split(SEPARATOR))
    return items


def activity_two():
    print('Generating the Total Price of each Product')
    items = get_items_from_file(PRODUCT_TABLE)
    with open(PRODUCT_VALUE_TABLE, 'w') as pvth:
        pvth.write(SEPARATOR.join(VALUE_COLUMNS) + '\n')  # header line
        for item_info in items:
            name = item_info[0]
            total_price = float(item_info[1]) * float(item_info[2])
            pvth.write('{}{}{:.2f}\n'.format(name, SEPARATOR, total_price))
        del name
        del total_price
    del items


def activity_three():
    print('Getting the Total of All Items')
    items = get_items_from_file(PRODUCT_VALUE_TABLE)
    total_value = 0
    for item in items:
        total_value += float(item[1])
    print('The total value of products in your inventory is {:.2f}'.format(total_value))


def main():
    activity_one()
    activity_two()
    activity_three()


if __name__ == '__main__':
    main()
