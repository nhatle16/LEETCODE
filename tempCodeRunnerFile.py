
    for i in range(len(shorter)-1, -1, -1):
        value = int(shorter[i]) + int(longer[i])
        if carry:
            value += 1
        if value == 3:
            value = 1
            carry = True
        elif value == 2:
            value = 0
            carry = True
        else:
            carry = False
        ans += str(value)
    if carry:
        ans += '1'
        
    return ans[::-1]