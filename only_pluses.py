for _ in range(int(input())):
    a,b,c = map(int,input().split())

    l = [a,b,c]

    n = 0
    while n<5:
        l.sort()
        l[0] = l[0] + 1
        n+=1

    print(l[0]*l[1]*l[2])