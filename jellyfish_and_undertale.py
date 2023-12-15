for _ in range(int(input())):
    a,b,n = map(int, input().split())
    x = list(map(int, input().split()))
    time = b

    for i in range(len(x)):
        if x[i] <= (a-1):
            time += x[i]
        else:
            time += (a-1)

    print(time)