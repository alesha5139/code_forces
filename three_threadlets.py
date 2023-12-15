import math
for _ in range(int(input())):
    a,b,c = map(int,input().split())

    gcd = math.gcd(a,b,c)

    if (a+b+c)/gcd > 6:
        print("NO")
    else:
        print("YES")



    
    