import time

def monitor_prediction_time():
    """
    A decorator to monitor and log the time taken by a function to execute.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()  # Record the start time
            result = func(*args, **kwargs)  # Execute the decorated function
            end_time = time.time()  # Record the end time
            print(f"Execution time for {func.__name__}: {end_time - start_time:.2f} seconds")
            return result
        return wrapper
    return decorator
