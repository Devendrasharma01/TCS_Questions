# Given a string S(input consisting) of ‘*’ and ‘#’. The length of the string is variable. The task is to find the minimum number of ‘*’ or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.

def check_string(string):
    no_hash = 0
    no_star = 0
    for char in string:
        if char == '*':
            no_star += 1
        elif char == '#':
            no_hash += 1
    difference = no_hash - no_star
        
    if difference == 0:
        result = 0
        print(f"{result} -> no of * and # are equal") 
    else:
        result = 1
        print(f"{result} -> no of * and # are not equal") 

input_string = input("Enter the string with spaces: ")
check_string(input_string)
   