# https://leetcode.com/problems/length-of-last-word/description/

def lengthOfLastWord(s: str) -> int:
    if len(s) == 0:
            return 0

    mylist = s.split()
    last_word = mylist[-1]
    count = 0
    
    while last_word:
        count += 1
        last_word = last_word[1:]

    return count