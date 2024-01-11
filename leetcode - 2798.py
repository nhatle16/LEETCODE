def employeeMetTarget(hours, target):
    num = 0
    for hour in hours:
        num += 1 if hour >= target else 0
    
    return num


hours = [0,1,2,3,4]
target = 3

print(employeeMetTarget(hours, target))