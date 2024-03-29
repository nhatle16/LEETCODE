# https://leetcode.com/problems/valid-parentheses/description/

# Using recursion
def isValid(s: str) -> bool:
    if len(s) == 0:
        return True
    
    bracket_dict = {'(': ')', '{': '}', '[': ']'}
    
    if bracket_dict.get(s[0]) == s[1]:
        return isValid(s[2:])
    
    return False

# Using stack
def isValid2(s: str) -> bool:
    bracket_dict = {')': '(', '}': '{', ']': '['}
        
    stack = []

    for char in s:
        if char in bracket_dict.values():
            stack.append(char)
        elif char in bracket_dict.keys():
            if not stack or bracket_dict[char] != stack.pop():
                return False

    return not stack

if __name__ == "__main__":
    brackets = input("Enter an expression of brackets: ")
    result = isValid2(brackets)
    
    print("Checking if {} is a valid expression, received {}".format(brackets, result))