# . Particulate matters are the biggest contributors to Delhi pollution. The main reason behind the increase in the concentration of PMs include vehicle emission by applying Odd Even concept for all types of vehicles. The vehicle with the odd last digit in the registration number will be allowed on roads on odd dates and those with even last digit will on even dates.
 #Given an integer array a[], contains the last digit of the registration number of N vehicles traveling on date D(a positive integer). The task is to calculate the total fine collected by the traffic police department from the vehicles violating the rules.

def find_odd_eve(array,date,fine):
    even_number = 0
    odd_number = 0
    for i in array:
        if i%2 == 0:
            even_number += 1
        elif i%2 != 0:
            odd_number += 1
    if date%2 == 0:
        print(f"The number plate is odd and the fine is: {odd_number*fine}")
    elif date%2 != 0:
        print(f"The number plate is even and the fine is: {even_number*fine}")

input_string = input("Enter the list with spaces: ")
input_list = input_string.split()
no_plate = [int(num) for num in input_list]
date = int(input("Enter the date: "))
fine = int(input("Enter the fine: "))
result = find_odd_eve(no_plate,date,fine)
