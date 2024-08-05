for _ in range(int(input())):
    n,k = map(int, input().split())

    grid= []
    for i in range(n):
        row = input()
        row_scaled = ''
        for x in range(0,n,k):
            row_scaled += row[0+x:k+x][0]

        if i%k == 0:
            grid.append(row_scaled)

        
    for r in grid:
        print(r)
                

