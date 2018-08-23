
def Print_Table(num):
    for n in range(1, 11):
        print(num, "X", n, "=", num*n)

num = int(input("Enter a number: "))
Print_Table(num)
