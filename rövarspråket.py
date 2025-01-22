word = input("Enter a word: ")
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
new_word = ""

for character in word.lower():
    if character in consonants:
        new_word += character + "o" + character
    
    else:
        new_word += character

print(new_word)