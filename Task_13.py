""" Find the 15th term of the series?
0,0,7,6,14,12,21,18, 28
Explanation : In this series the odd term is increment of 7 {0, 7, 14, 21, 28, 35 – – – – – – }
And even term is a increment of 6 {0, 6, 12, 18, 24, 30 – – – – – – } """

def get_term(num):
    if num <= 0:
        raise ValueError("Term number must be positive.")

    return (num // 2) * 7 if num % 2 == 1 else (num // 2) * 6

term = get_term(15)
print(f"The 15th term of the series is: {term}")