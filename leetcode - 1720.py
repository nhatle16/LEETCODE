def decode(encoded, first):
    ans = []
    ans.append(first)
    for i in range(len(encoded)):
        val = encoded[i] ^ ans[i] 
        ans.append(val)

    return ans

encode = [6]
first = 1

print(decode(encode, first))