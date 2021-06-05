# cook your dish here
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

t = int(input())
for i in range(t):
    print(factorial(int(input())))