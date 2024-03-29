def maxPower(s):
    if len(s) == 0:
        return 0
    
    max_len, cur_len = 1, 1
    
    for i in range(0, len(s)-1):
        cur_len = cur_len + 1 if (s[i] == s[i+1]) else 1
        max_len = max(cur_len, max_len)

    return max_len

s1 = "leetcode"
s2 = ""
s3 = "minhnhaaat"

print(maxPower(s3))