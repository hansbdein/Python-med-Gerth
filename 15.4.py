
'''

def enforce_types(*decorator_args):
    def decorator(f):
        def wrapper(*args):
            assert len(args) == len(decorator_args),\
                ("got %s arguments, expected %s" % (len(args), len(decorator_args)))
            assert all([isinstance(x, t) for x, t in zip(args, decorator_args)]),\
                "unexpected types"
            return f(*args)
        return wrapper
    return decorator
@enforce_types(str, int) # decorator with arguments
def print_repeated(txt, n):
    print(txt * n)
print(print_repeated("Hello ", 3))
print(print_repeated("Hello ", "world"))
'''


def compose(*decorator_args): # decorator function

    def decorator(f):

        def wrapper(*args,dargs=decorator_args):
            
            if len(dargs)==0:
            
                return f
            else:
           
                return dargs[0](wrapper(*args,dargs=dargs[1:]))
            
        return wrapper
    return decorator

def compose_rec(*decorators):
    def nested_decorator_rec(f,decs = decorators):
        if len(decs) == 0:
            return f
        return nested_decorator_rec(decs[-1](f),decs[:-1])
    return nested_decorator_rec


def double(f):
    def wrapper(*args):
        return 2 * f(*args)

    return wrapper

def add_three(f):
    def wrapper(*args):
        return 3 + f(*args)

    return wrapper

compose(add_three, double, add_three)
def seven(): return 7

print(seven())  # prints 23

my_decorator = compose(add_three, double, add_three)

@my_decorator
def seven(): return 7

print(seven())  # prints 23