

word = input('Enter a word to know if its a palindrom :')

reverse = word[::-1]

if reverse == word:
    print("Word entered is a palindrom")
else:
    print("Word not a palindrom")    