def countMatches(items, ruleKey, ruleValue):
    match = 0
    for i in range(len(items)):
        if ruleKey == "type" and ruleValue == items[i][0]:
            match += 1
        elif ruleKey == "color" and ruleValue == items[i][1]:
            match += 1
        elif ruleKey == "name" and ruleValue == items[i][2]:
            match += 1

    return match

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
key = "type"
value = "phone"

print(countMatches(items, key, value))