def fib(n):
    if n>1:
        return fib(n-1)+fib(n-2)
    elif n==1:
        return "b"
    elif n==0:
        return "a"
    else:
        raise AssertionError("geen natuurlijk getal", n)
try:
    s = input()
    n = int(s)
    if n<0:
        raise AssertionError("geen natuurlijk getal", n)
    print(fib(n))
except Exception as error:
    print('Error: ' + repr(error))