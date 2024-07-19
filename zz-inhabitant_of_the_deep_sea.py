# Times outs
for t in range(int(input())):
    n,k = map(int,input().split())
    ships = list(map(int,input().split()))

    while k > 0 and len(ships) > 0:
        m = min(ships[0],ships[-1])
        if k >= 2*m:
            ships[0] -= m
            ships[-1] -= m
            k -= 2*m
        else:
            ships[0] -= k//2
            if k%2 == 1:
                ships[0] -= 1
            ships[-1] -= k//2
            k = 0

        if len(ships) > 0:
            if ships[0] <= 0:
                ships.pop(0)
        if len(ships) > 0:
            if ships[-1] <= 0:
                ships.pop(-1)
    
    print(n-len(ships))