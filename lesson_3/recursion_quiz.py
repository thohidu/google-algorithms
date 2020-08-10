"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1   
    else:
        return get_fib(position - 1) + get_fib(position - 2)



"""position 2
                    get_fibo(1)       +       get_fibo(0)
                        1             +            0
                        return        1

   position 3
                    get_fibo(2)                  +                   get_fibo(1)
            get_fibo(1)+ get_fibo(0)             +                       1    
                 1     +    0
                                                 2
    
      
"""


if __name__ == "__main__":
    # Test cases 
    print(get_fib(9))
    print(get_fib(11))
    print(get_fib(0))
    

