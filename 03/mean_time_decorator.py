import time

def mean(k=5):
    def mean_decorator(func):
        calls = []
        def wrapper(*argc, **kwargs):
            start = time.time()
            res = func(*argc, **kwargs)
            end = time.time()
            
            if len(calls) == k:
                calls.pop(0)
            calls.append(end - start)
            print("Среднее время работы", func.__name__, "за последние", k, "вызовов", round(sum(calls) / len(calls), 4))
            print('-' * 30)
            return res
        
        return wrapper
    
    return mean_decorator

@mean(5)
def sum_comp(n):
    arr = [i for i in range(n)]
    return sum(arr)

@mean(5)
def sum_append(n):
    arr = []
    for i in range(n):
        arr.append(i)
    return sum(arr)

ARRAY_SIZE = 10**6

for i in range(7):
    sum_comp(ARRAY_SIZE)
    sum_append(ARRAY_SIZE)
