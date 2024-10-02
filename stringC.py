
def compress(word):
    compressed = ""
    words = list(word)
    i = 0
    
    for letter in words:
       
        occurence = 0
        
        while i < len(words):
            if words[i] == letter:
                occurence += 1
            
                i += 1
            else:
                break
            
            
        if occurence > 0:
            compressed += letter + str(occurence) 
    
    
    return compressed


userInput = input("Enter a string: ")

print(compress(userInput))









    
