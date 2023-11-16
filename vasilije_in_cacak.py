for _ in range(int(input())):
    n,k,x = map(int, input().split())
    min_sum = (k-1)*(k)/2
    max_sum = k*n - min_sum
    

    if max_sum >= x and min_sum < x and (x-min_sum) >= k:
        print("YES")
    else:
        print("NO")
    