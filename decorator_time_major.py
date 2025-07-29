
from time import time


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func():
        t1 = time()
        print("Starting excutios: " ,t1)
        result = func()
        t2 = time()
        print("Endexcution time: ",(t2))
        print(f'Function executed in {(t2-t1):.2}')
        return result
    return wrap_func


@timer_func
#This is only operation for give this to decorator function
def Operation_func():
    for i in range(10):
        for j in range(100000):
            i*j

start_deco_time = time()
Operation_func()
