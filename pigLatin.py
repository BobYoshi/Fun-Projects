word = input("Input a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']

if word[0] in vowels:
    word += "ay"
else:
    word = word[1:] + word[0] + "ay"
    
print(word)
