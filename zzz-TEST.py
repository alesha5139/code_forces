x = [1,2,5,4,3]
y = [1,4,25,16,9]

z = []

for i in range(len(x)):
    z += [[[y[i]/x[i]], [i]]]

print(z)
z.sort()
print(z)