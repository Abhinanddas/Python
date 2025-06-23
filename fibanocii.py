def get_fib(position):
    
    if position <=1:
        return position
    else:
        return get_fib(position-1) + get_fib(position - 2)



print(get_fib(0))
