# PyThreadFuture

PyThreadFuture is a Python class that simplifies running tasks asynchronously using a ThreadPoolExecutor. It offers two decorator methods for executing functions in separate threads, along with methods for waiting for and retrieving results from multiple futures.

## Features

- **async_task_no_return**: Decorator for running a task asynchronously without its result.
- **async_task_return**: Decorator for running a task asynchronously and returning a Future object for retrieving the result later.
- **run_and_wait**: Method to wait for and retrieve results from multiple futures.
- **shutdown**: Method to shut down the ThreadPoolExecutor, ensuring resource cleanup.

## Usage

# PyThreadFuture Usage Examples

This README provides detailed examples of using the PyThreadFuture library to execute asynchronous tasks in Python.

## Overview

PyThreadFuture simplifies asynchronous task execution by providing decorators for running functions in separate threads. It also offers utilities for managing and gathering results from multiple asynchronous tasks.

## Installation

First, install the PyThreadFuture library using pip:

```bash
pip install PyThreadFuture
Usage
Initialization
Initialize the PyThreadFuture executor at the top of your file:

python
Copy code
from time import sleep
from PyThreadFuture import PyThreadFuture

executor = PyThreadFuture()
Class Methods
You can use PyThreadFuture with class methods. Here's an example:

python
Copy code
class TestingClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    @executor.async_null_result
    def test_function1(self):
        print(f"Class test_function1 async_null_result")
        sleep(10)  # Simulate a time-consuming operation
        self.a = 100

    # Other class methods...

testing_class = TestingClass()

testing_class.test_function1()
# Continue immediately without waiting for test_function to complete.
print("Continuing after class method with async_null_result...")

# Submit tasks to the executor
instance_future1 = testing_class.test_function3()
instance_future2 = testing_class.test_function4()

# Wait for all submitted tasks to complete and get their results
result = executor.run_and_wait([instance_future1, instance_future2])
print(f"Class instance result:{result}")
# Continue immediately without waiting for class methods to complete.
print("Continuing after class methods...")
Standalone Functions
You can also use PyThreadFuture with standalone functions:

python
Copy code
@executor.async_null_result
def test_function1(a, b):
    print(f"test_function1 async_null_result")
    sleep(10)  # Simulate a time-consuming operation
    return a + b

# Other functions...

test_function1(10, 10)
# Continue immediately without waiting for function call to complete.
print("Continuing after function call with async_null_result...")

# Submit tasks to the executor
future3 = test_function3(30, 30)
future4 = test_function4(40, 40)

# Wait for all submitted tasks to complete and get their results
result = executor.run_and_wait([future3, future4])
print(result)
Shutdown
Don't forget to shut down the executor to release resources:

python
Copy code
executor.shutdown()
License
This project is licensed under the MIT License. See the LICENSE file for details.

Copy code
This markdown file serves as a concise guide for users interested in leveraging the PyThreadFuture class for asynchronous task execution. It outlines the features, usage instructions, and provides an example for better understanding. Additionally, it includes licensing information for clarity on usage rights.
