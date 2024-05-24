''' The program will receive 3 English words inputs from STDIN 
1. These three words will be read one at a time, in three separate line 
2. The first word should be changed like all vowels should be replaced by * 
3. The second word should be changed like all consonants should be replaced by @ 
4. The third word should be changed like all char should be converted to upper case 
5. Then concatenate the three words and print them '''

def modify_word(word, vowels="aeiou", consonants="bcdfghjklmnpqrstvwxyz"):
    modified_word = ""
    for char in word:
        if char.lower() in vowels:
            modified_word += "*"
        elif char.lower() in consonants:
            modified_word += "@"
        else:
            modified_word += char
    return modified_word.upper()

word1 = input("Enter the 1st word: ").strip()
word2 = input("Enter the 2nd word: ").strip()
word3 = input("Enter the 3rd word: ").strip()
modified_word = modify_word(word1) +  modify_word(word2) + modify_word(word3) 
print(modified_word)