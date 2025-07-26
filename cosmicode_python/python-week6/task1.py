import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time=time.time()
        total_time=end_time-start_time
        print(f"execution time of {func.__name__}: {total_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def multiply(number):
    result=1
    for i in range(len(number)):
        result*=number[i]
    return result

mul_result=multiply([1,5,7,9,10])
print("Result: ",mul_result)