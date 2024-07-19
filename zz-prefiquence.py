### I have oversimplified this because it matters the order of digits
### EX: a = 1001, b = 1010
### The actual answer is 3, but my code would give 4 since it allows for rearanging
### Real solution can not allow for the rearangemnt
### I don't know how to check this

### I have solved the previous problem, but the new problem is runtime
### This is probably because I check the sub string for every value of k up to the right answer
### This means that if the final value of k is too high, it will need to run through the string way too many times

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

for t in range(int(input())):
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
            k += 1
        else:
            end = True

    print(k)


    