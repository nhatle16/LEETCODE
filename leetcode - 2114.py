def mostWordsFound(sentences):  
    max_len = 0
    for sentence in sentences:
        length = len(sentence.split())
        if max_len < length:
            max_len = length

    return max_len

sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]

print(mostWordsFound(sentences))