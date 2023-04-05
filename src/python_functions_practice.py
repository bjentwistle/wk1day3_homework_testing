def return_10():
    return 10

def add(a, b):
    add_result = a + b
    return add_result

def subtract(x, y):
    subract_result = x - y
    return subract_result

def multiply(first_multiplier, second_multiplier):
    multiply_result = first_multiplier * second_multiplier
    return multiply_result

def divide(first_divisor, second_divisor):
    divide_result = first_divisor/second_divisor
    return divide_result

def length_of_string(test_string):
    string_length = len(test_string)
    return string_length

def join_string(string_1, string_2):
    joined_string = string_1+string_2 
    return joined_string

def add_string_as_number(first_string_num, second_string_num):
    add_result = int(first_string_num)+ int(second_string_num)
    return add_result

def number_to_full_month_name(month_number):
    months_as_full_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    result = months_as_full_name[month_number-1]
    return result

def number_to_short_month_name(month_number):
    months_as_short_name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    result = months_as_short_name[month_number-1]
    return result

#Further work

def volume_of_cube(side_length): 
    volume_value = side_length**3
    return volume_value

""" 
From W3 schools site:
Create a slice that starts at the end of the string, and moves backwards.
In this particular example, the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.
"""
def reverse_string(given_string):
    reversed_string = given_string[::-1] 

    return reversed_string

def convert_to_celsius(temp_in_fahrenheit):
    celsius = int((temp_in_fahrenheit - 32)*5/9) #forced to integer so no chance of error due to decimal places 
    return celsius