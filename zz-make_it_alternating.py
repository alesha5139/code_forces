import math
for _ in range(int(input())):
    s = input()
    removals = 0
    repeats = 1
    permutations = 0

    prev = s[0]
    for i in range(1,len(s)):
        if s[i] == prev:
            removals += 1
            repeats += 1
        elif repeats > 1:
            permutations = permutations % 998244353
            permutations += math.factorial(repeats)
            repeats = 1
        prev = s[i]
    if removals == 0:
        permutations = 1
    elif repeats>1:
        permutations = permutations % 998244353
        permutations += math.factorial(repeats)

    print(removals, permutations)