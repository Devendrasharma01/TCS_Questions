# At a fun fair, a street vendor is selling different colors of balloons. He sells N numbers of different colors of balloons (B[]). The task is to find the color (odd) of the balloon which is present an odd number of times in the bunch of balloons.

from collections import Counter

def find_odd(baloon_colour):
    colour_counts = Counter(baloon_colour)
    for colour,count in colour_counts.items():
        if count %2 != 0:
            return colour
    return "All are even"

input_string = input("Enter the colour of boloon with spaces: ")
baloon_colour = input_string.split() 
print(baloon_colour)
odd_colour = find_odd(baloon_colour)
print(f"{odd_colour}->{baloon_colour} -> {odd_colour} color balloon is present an odd number of times in the bunch.")

        