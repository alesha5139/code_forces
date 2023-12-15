s = input()

def danger_check(lst):
    count = 1
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            count += 1
        else:
            count = 1
        
        if count >= 7:
            return "YES"
    return "NO"

print(danger_check(s))
            