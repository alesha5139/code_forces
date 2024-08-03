for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    operations = 0

    while len(a) > 1:
        operations += (a.pop()*2-1)

    print(operations)