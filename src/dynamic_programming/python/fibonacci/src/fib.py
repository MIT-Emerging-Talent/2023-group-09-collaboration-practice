def fib_basic(n):
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_basic(n - 2) + fib_basic(n - 1)


def fib_memo(n, memo=dict()):
    
    if n < 1:
        return 0
    if n <= 2:
        return 1
    return memo.get(n, fib_memo(n - 1, memo) + fib_memo(n - 2, memo))


def fib_tab(n):
    
    if n < 1:
        return 0

    if n == 1:
        return 1

    table = [0] * (n + 1)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]

####
### Gloire
def fib_basic(n):
    """
     This is a recursive function that finds the nth number in the Fibonacci sequence by recursively 
     calculating the
     (n-1) and (n-2)th numbers in the sequence
     returns fib(n)
    """
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fib_basic(n-1)+ fib_basic(n-2)

#fibdic = {}
def fib_memo(n, memo = {}):
    """
    This function uses memoization to store the results of subproblems and avoid recalculating them.
    It works similarly to the fib_basic() function, but it uses a dictionary to store the results of subproblems
    so that they can be reused in future recursive calls.
    returns the fib(n)
    
    """
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo) 
        memo[n] = result 
        return result
    
def fib_tab(n):
    """
    This function uses dynamic programming to store the results of subproblems in a table.
    It iteratively calculates the nth number in the Fibonacci sequence by using the values of the (n-1)th
    and $(n - 2)th $numbers in the sequence
    returns a list of fib numbers
    """
    
    if n<= 1:
        return n
    
    table = [0] * (n+1)
    table[1] = 1
    
    for i in range(2,n+1):
        table[i] = table[i-1]+table[i-2]
        
    return table
