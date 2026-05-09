import time

def cache(func):
    chache_value ={}
    print(chache_value)
    def wrapper(*args):
        if args in chache_value:
            return chache_value[args]
        result =func(*args)
        chache_value[args]= result
        return result
     
    return wrapper





@cache
def long_running_function(a,b):
    time.sleep(4)
    return a +b


print(long_running_function(5,4))
print(long_running_function(5,4))