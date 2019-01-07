# find sum of even fibonacci numbers less than 4m
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
   
def fib_list(n):
    l = [fibonacci(x) for x in range(35) if fibonacci(x) < n]
    return l

def sum_even_fib_list(n):
    print(sum([x for x in fib_list(n) if x%2==0]))


sum_even_fib_list(5000000)
