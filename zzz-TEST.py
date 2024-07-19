### I have oversimplified this because it matters the order of digits
### EX: a = 1001, b = 1010
### The actual answer is 3, but my code would give 4 since it allows for rearanging
### Real solution can not allow for the rearangemnt
### I don't know how to check this

def is_sub(x,y):
    len_x = len(x)
    len_y = len(y)
    i,j = 0,0

    while i < len_x and j < len_y:
        if x[i] == y[j]:
            i += 1
        j += 1
    
    if i == len_x:
        return True
    else:
        return False

n,m = map(int, input().split())
a = input()
b = input()

count_b_1 = 0
count_b_0 = 0
for i in b:
    if i == '1':
        count_b_1 += 1
    else:
        count_b_0 += 1

k = 0
end = False
while not end and k < n:
    sub_a = a[:k+1]
    if is_sub(sub_a,b):
        print(f'sub:{sub_a}')
        k += 1
    else:
        end = True

print(k)