import time
def cal_time(func):
    def wrapper(*args,**kwargs):
        t1=time.perf_counter()
        result=func(*args,**kwargs)
        t2=time.perf_counter()
        print("%s running time: %s sec." %(func.__name__,t2-t1))
        return result
    return wrapper