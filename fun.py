for _ in range(int(input())):
    n,x = map(int, input().split())

    count = 0

    for a in range(1,n):
        for b in range(1,int(n/a)):
            ub = int(min((n-a*b)/(a+b),(x-a-b)))
            if ub >= 1:
                count += ub

    print(count)
