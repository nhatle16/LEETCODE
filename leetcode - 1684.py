def countConsistentString(allowed, words):
    ans = len(words)

    for word in words:
        temp = set(word)
        for char in temp:
            if char not in allowed:
                ans -= 1
                break
                
    return ans

if __name__ == "__main__":
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    print(countConsistentString(allowed, words))