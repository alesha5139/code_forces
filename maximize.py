import math

for t in range(int(input())):
    x = int(input())

    c_max = 0
    i_max = 0
    for i in range(1,x):
        temp = math.gcd(x,i) + i
        if temp > c_max:
            c_max = temp
            i_max = i

    print(i_max)