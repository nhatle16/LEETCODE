# https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(strs: list[str]) -> str:
    ans = ""
    if not strs:    return ans
    
    # sort the list lexicographically 
    strs = sorted(strs)
    
    first = strs[0]
    last = strs[-1]
    
    # iterate from the begin 'til the length of the short string
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans  # return if there is no common prefix
        ans += first[i]
        
    return ans
    
    
if __name__ == "__main__":
    input = ["nolan", "nice", "nominal"]
    result = longestCommonPrefix(input)
    
    print(result)
