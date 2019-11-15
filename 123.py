list = []

for n in range(10**3):
    i, j, b = 1, 1, set()
    while n-2*i >= 0:
        b.add(2*list[n-i]-list[n-2*i])
        i += 1
        while j in b:
            b.remove(j)
            j += 1

    list.append(j) 
print(list)