def finalValAfterOperations(operations):
    val = 0
    for i in operations:
        val = val-1 if (i == "X--" or i == "--X") else val+1
    return val

command = ["X--", "X++", "++X", "X++", "X++"]

print(finalValAfterOperations(command))