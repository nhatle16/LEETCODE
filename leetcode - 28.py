# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

def indexOfFirstOccur(haystack: str, needle: str) -> int:
    length = len(needle)
    res = -1
    # iterate through each character
    for i in range(len(haystack)):
        if i+length-1 < len(haystack):    # check if the last character is not out of range
            word = haystack[i:i+length]
            if word == needle:
                res = i
                return res
        else:
            return res
            
    return res

if __name__ == "__main__":
    haystack = "iamthebestguyamongguysnamednolan"
    needle = "nolan"
    result = indexOfFirstOccur(haystack, needle)
    
    print(result)