def restoreString(s,indices):
    if len(s) != len(indices) or max(indices) > len(s):
        return None
    
    lis = [0] * len(indices)
    
    for letter, idx in zip(s, indices):
        lis[idx] = letter
        
    return ''.join(lis)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(restoreString(s, indices))