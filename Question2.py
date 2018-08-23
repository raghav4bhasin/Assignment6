def Perfect(num):
    add = 0

    for x in range (1, num):
        if num % x is 0:
            add = add + x
    if add is num:
        return add
    else:
        return 0

print("Perfect numbers:- ")
for i in range(1, 1001):
    n = Perfect(i)
    if n is not 0:
        print(n)
    

