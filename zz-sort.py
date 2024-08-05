for _ in range(int(input())):
    n,q = map(int, input().split())
    a = input()
    b = input()

    pref_a = {}
    pref_b = {}

    for x in range(n):
        tmp_a = [0]*(n+1)
        tmp_b = [0]*(n+1)
        for i in range(n):
            if a[i] == a[x]:
                tmp_a[i+1] = 1
            if b[i] == b[x]:
                tmp_b[i+1] = 1

        for i in range(n):
            tmp_a[i+1] += tmp_a[i]  
            tmp_b[i+1] += tmp_b[i]
        pref_a[a[x]] = tmp_a
        pref_b[b[x]] = tmp_b  

    for query in range(q):
        l,r = map(int, input().split())
        count = 0
        seen = []
        for char in a:
            if char not in seen:
                try:
                    diff = (pref_a[char][r]-pref_a[char][l-1])-(pref_b[char][r]-pref_b[char][l-1])
                    if diff > 0:
                        count += diff
                    #print('diff '+str(diff))
                    #print('cound '+str(count))
                except:
                    #print(char)
                    count += 1
                    #print(count)
                seen.append(char)
        
        
        print(int(count))