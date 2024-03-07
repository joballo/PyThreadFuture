from concurrent.futures import ThreadPoolExecutor, as_completed
import functools

class PyThreadFuture:
    """
    A class that simplifies running tasks asynchronously using a ThreadPoolExecutor.
    
    This class provides two decorator methods for executing functions in separate threads:
    - async_task_no_return: Executes a function asynchronously. It is designed for tasks
      where the return value is not needed.
    - async_task_return: Executes a function asynchronously and returns a Future object,
      allowing the caller to retrieve the result at a later time.

    The class also offers a method to wait for and retrieve results from multiple futures,
    making it easier to manage the execution of concurrent tasks.

    Methods:
    - __init__(self): Initializes the AsyncExecutor with a ThreadPoolExecutor.
    - async_task_no_return(self, function): Decorator for running a task asynchronously
      without its result.
    example:
           @executor.async_task_no_return
            def test_function2():
                sleep(10)  # Simulate a time-consuming operation
                print("test_function2")

            @executor.async_task_no_return
            def test_function2():
                sleep(1)  # Simulate a time-consuming operation
                print("test_function2")
      
    - async_task_return(self, function): Decorator for running a task asynchronously,
      returning a Future object for retrieving the task's result later.
    - run_and_wait(self, futures): Waits for the specified futures to complete and returns
      their results as a list.
    example:
            # Submit tasks to the executor
            future1 = test_function1(5, 10)
            future2 = test_function2(5, 10)

            # Wait for all submitted tasks to complete and get their results
            executor.run_and_wait([future1, future2])

    - shutdown(self): Shuts down the ThreadPoolExecutor, ensuring that all resources are
      freed.

    Usage:
    Create an instance of AsyncExecutor and use the provided decorators to run functions
    asynchronously. Use `run_and_wait` if you need to wait for multiple tasks to complete
    and gather their results. Call `shutdown` when done to clean up resources.
    """
    def __init__(self):
        self.executor = ThreadPoolExecutor()

    def async_null_result(self, function):
        """Decorator to run a function asynchronously without waiting for a response."""
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            self.executor.submit(function, *args, **kwargs)
        return wrapper

    def async_data_handler(self, function):
        """Decorator method to run a function asynchronously in a separate thread."""
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            future = self.executor.submit(function, *args, **kwargs)
            return future
        return wrapper

    def run_and_wait(self, futures):
        """Wait for all submitted tasks to complete and return their results."""
        results = []
        for future in as_completed(futures):
            results.append(future.result())
        return results

    def shutdown(self):
        """Shuts down the executor, freeing any resources."""
        self.executor.shutdown()