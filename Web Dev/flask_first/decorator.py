import time

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        name = function.__name__
        print(f"You called {name}{args}")
        result = function(args)
    return wrapper

def speed_calc_decorator(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        speed = end - start
        return speed
    return wrapper
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

