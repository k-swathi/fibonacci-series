num = {}
def fib(n):
    if n in num:
        return num[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    num[n]=f
    return f
number=int(input("enter the range"))
print( fib(number)) 
