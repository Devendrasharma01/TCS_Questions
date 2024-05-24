''' One programming language has the following keywords that cannot be used as identifiers: break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var.
Write a program to find if the given word is a keyword or not'''

keyword = ["break", "case", "continue", "default", "defer", "else", "for", "func", "goto", "if", "map", "range", "return", "struct", "type", "var"]

def is_keyword(word):
    return word.lower() in keyword

word = input("Enter a word: ")

if is_keyword(word):
    print(f"{word} is a keyword")
else:
    print(f"{word} is not a keyword")