# Times out

for t in range(int(input())):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    count = 0

    for x in range(len(a)-len(b)+1):
        sub = a[x:(x+len(b))]
        
        temp_b = b.copy()
        k_count = 0
        i = 0
        for i in sub:
            if i in temp_b:
                temp_b.remove(i)
                k_count += 1
        
        #print(f'{sub}: {k_count}')
        if k_count >= k:
            count += 1
    
    print(count)