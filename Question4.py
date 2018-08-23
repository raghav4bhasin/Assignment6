def Power(m, n):
    if n is 1:
        return m
    if n is not 1:
        return (m * Power(m, n-1))

num = int(input("Enter a number: "))
exp = int(input("Enter exponential: "))
print("Result: ",Power(num, exp))

