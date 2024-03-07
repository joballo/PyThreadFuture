# PyThreadFuture

PyThreadFuture is a Python class that simplifies running tasks asynchronously using a ThreadPoolExecutor. It offers two decorator methods for executing functions in separate threads, along with methods for waiting for and retrieving results from multiple futures.

## Features

- **async_task_no_return**: Decorator for running a task asynchronously without its result.
- **async_task_return**: Decorator for running a task asynchronously and returning a Future object for retrieving the result later.
- **run_and_wait**: Method to wait for and retrieve results from multiple futures.
- **shutdown**: Method to shut down the ThreadPoolExecutor, ensuring resource cleanup.

## Usage

1. **Initialization**: Create an instance of `PyThreadFuture`.
```python
executor = PyThreadFuture()
Decorators: Use decorators to run functions asynchronously.
python
Copy code
@executor.async_null_result
def task1():
    # Task logic here
python
Copy code
@executor.async_data_handler
def task2():
    # Task logic here
Wait for Results: Use run_and_wait to wait for multiple tasks to complete and gather their results.
python
Copy code
future1 = task1()
future2 = task2()
executor.run_and_wait([future1, future2])
Shutdown: Call shutdown when done to clean up resources.
python
Copy code
executor.shutdown()
Example
python
Copy code
from time import sleep

executor = PyThreadFuture()

@executor.async_null_result
def example_task1():
    sleep(5)
    print("Task 1 completed")

@executor.async_data_handler
def example_task2():
    sleep(3)
    return "Task 2 completed"

future1 = example_task1()
future2 = example_task2()
results = executor.run_and_wait([future1, future2])
print("Results:", results)

executor.shutdown()
License
This project is licensed under the MIT License. See the LICENSE file for details.

Copy code
This markdown file serves as a concise guide for users interested in leveraging the PyThreadFuture class for asynchronous task execution. It outlines the features, usage instructions, and provides an example for better understanding. Additionally, it includes licensing information for clarity on usage rights.
