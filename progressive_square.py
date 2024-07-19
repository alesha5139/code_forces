for t in range(int(input())):
    n,c,d = map(int,input().split())
    b = sorted(list(map(int,input().split())))
    
    prog_sqr = [b[0]]
    for i in range(2,n**2+1):
        if i%(n) == 1:
            prog_sqr.append(prog_sqr[i-n-1]+c)
        else:
            prog_sqr.append(prog_sqr[i-2]+d)
    
    prog_sqr = sorted(prog_sqr)
    
    
    if prog_sqr == b:
        print("Yes")
    else:
        print("No")