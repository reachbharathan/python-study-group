def fib(n):
    if(n==0):
        return 0
    elif(n<2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter the no.of terms"))
for i in range(n):
    print("fibonacci series",fib(i))