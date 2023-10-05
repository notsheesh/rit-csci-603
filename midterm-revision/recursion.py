# factorial
def fact0():
    return 1

def fact1():
    return 1

def fact2():
    return 2 * fact1()

def fact3():
    return 3 * fact2()

def factn(n):
    if n <= 1:
        return 1
    else:
        return n * factn(n-1)
    
def fact_iter(n):
    acc = 1
    while n > 1: 
        acc = acc * n
        n -= 1
    return acc
    
def fact_tail(n, acc):
    if n <= 1:
        return acc
    else:
        return fact_tail(n = n-1, acc = acc * n)
    
print("factorial")
for i in range(5):
    print(fact_iter(i), factn(i), fact_tail(i, 1))

def fibo0():
    return 0

def fibo1():
    return 1

def fibo2():
    return fibo0() + fibo1()

def fibo3():
    return fibo2() + fibo1()

def fibo4():
    return fibo3() + fibo2()

# 0 1 1 2 3 5 8 13 ... 

def fibo(n):
    if n == 0 or n == 1: 
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_iter(n):
    prev = 0 
    curr = 1
    while n > 1:
        prev_temp = curr 
        curr = prev + curr
        prev = prev_temp
        n -= 1

    if n == 0: 
        return 0
    else: 
        result = curr

    return result

def fibo_acc(n, prev, curr):
    if n == 0: 
        return prev
    elif n == 1:
        return curr
    else:
        return fibo_acc(n-1, curr, curr+prev)

print("fibo")
for i in range(5):
    print(fibo_iter(i), fibo(i), fibo_acc(i, 0, 1))