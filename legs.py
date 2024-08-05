for _ in range(int(input())):
    n = int(input())
    cows = n//4
    chickens = (n-cows*4)//2
    print(cows+chickens)