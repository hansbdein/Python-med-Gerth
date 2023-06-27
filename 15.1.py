# -*- coding: utf-8 -*-



def enforce_integer_return(f): # decorator function
    def wrapper(*args):
        result=f(*args)
        assert isinstance(result,int),\
            "result must be int"
        return result
    return wrapper

@enforce_integer_return
def my_sum(x, y):
    return x + y






print(my_sum(19, 23))


print(my_sum(1, 2.5))
