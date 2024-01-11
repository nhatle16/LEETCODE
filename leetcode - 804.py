def uniqueMorseRepresent(words):
    ans = []
    morse_lis = [".-","-...","-.-.","-..",".","..-.",
                 "--.","....","..",".---","-.-",".-..",
                 "--","-.","---",".--.","--.-",".-.","...",
                 "-","..-","...-",".--","-..-","-.--","--.."]
    
    for word in words:
        code = ""
        for char in word:
            print(ord(char))
            code += morse_lis[ord(char)-97] 
        
        if code not in ans:
            ans.append(code)
    print(ans)
    return len(ans)
            
    
words = ["gin","zen","gig","msg"]
print(uniqueMorseRepresent(words))