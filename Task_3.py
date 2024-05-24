# An international round table conference will be held in india. Presidents from all over the world representing their respective countries will be attending the conference. The task is to find the possible number of ways(P) to make the N members sit around the circular table such that.
# The president and prime minister of India will always sit next to each other.

def seating_arrangements(n):
    if n <= 1:
        return 0
    effective_members = n-1
    arrangements = factorial(effective_members)
    unit_arrangements = 2
    return arrangements * unit_arrangements

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
no_of_members = int(input("Enter the numbers of members: "))
possible_arrangements = seating_arrangements(no_of_members)
print(f"The possible arrangements is: {possible_arrangements}")