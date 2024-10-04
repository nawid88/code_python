def palindrome(word):
    word = list(word)
    reverseWord = []
    for i in range(-1, -1*len(word)-1, -1):
        reverseWord += word[i]
    if reverseWord == word:
        return True
    else:
        return False
    


word = input("Enter a word: ")

if palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome")
