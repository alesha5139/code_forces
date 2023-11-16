for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = min(b)
    r = min(a)

    least_c = n*c + sum(a)
    least_r = n*r + sum(b)

    print(min(least_c,least_r))

