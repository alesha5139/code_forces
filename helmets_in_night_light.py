for _ in range(int(input())):
    n,p = map(int, input().split())
    share_num = list(map(int, input().split()))
    share_cost = list(map(int, input().split()))
    share_comb = []

    for i in range(n):
        share_comb += [[share_cost[i], share_num[i]]]

    share_comb.sort()

    index = 0
    share = 0
    known = 0
    price = p

    while known < (n-1):
        if share_comb[index][0] < p:
            if share < share_comb[index][1]:
                price += share_comb[index][0]
                known += 1
                share += 1
            else:
                index += 1
                share = 0
        else:
            price += p
            known += 1       

    print(price) 