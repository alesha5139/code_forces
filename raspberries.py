for _ in range(int(input())):
    n,k = map(int, input().split())
    lst = list(map(int, input().split()))

    min_diff = k

    if k!= 4:
        for i in range(n):
            diff = k-(lst[i]%k)
            if diff == k:
                min_diff = 0
            elif diff < min_diff:
                min_diff = diff
    else:
        even = 0

        for i in range(n):
            diff = k-(lst[i]%k)
            if diff == k:
                min_diff = 0
            elif diff < min_diff:
                min_diff = diff
            
            if lst[i]%2 == 0:
                even += 1
                    
        if even >= 2:
            four_diff = 0
        elif even == 1:
            four_diff = 1
        else:
            four_diff = 2

        min_diff = min(min_diff, four_diff)

    print(min_diff)