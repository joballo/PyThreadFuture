# PyThreadFuture

PyThreadFuture is a Python class that simplifies running tasks asynchronously using a ThreadPoolExecutor. It offers two decorator methods for executing functions in separate threads, along with methods for waiting for and retrieving results from multiple futures.

## Features

- **async_task_no_return**: Decorator for running a task asynchronously without its result.
- **async_task_return**: Decorator for running a task asynchronously and returning a Future object for retrieving the result later.
- **run_and_wait**: Method to wait for and retrieve results from multiple futures.
- **shutdown**: Method to shut down the ThreadPoolExecutor, ensuring resource cleanup.

## Usage

from time import sleep
from PyThreadFuture import PyThreadFuture
# Initilaize the PyThreadFuture at the top of the file
executor = PyThreadFuture()

class TestingClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    @executor.async_null_result
    def test_function1(self):
        print(f"Class test_function1 async_null_result")
        sleep(10)  # Simulate a time-consuming operation
        self.a = 100

    @executor.async_null_result
    def test_function2(self):
        print(f"Class test_function2 async_null_result")
        sleep(1)  # Simulate a time-consuming operation
        self.b = 200

    @executor.async_data_handler
    def test_function3(self):
        print(f"Class test_function3 async_data_handler")
        sleep(15)  # Simulate a time-consuming operation
        return self.a

    @executor.async_data_handler
    def test_function4(self):
        print(f"Class test_function4 async_data_handler")
        sleep(2)  # Simulate a time-consuming operation
        return self.b

testingclass=TestingClass()

testingclass.test_function1()
testingclass.test_function2()

# The main program continues immediately without waiting for test_function to complete.
print("Continuing after class method with async_null_result...")

instance_future1 = testingclass.test_function3()
instance_future2 = testingclass.test_function4()

# Wait for all submitted tasks to complete and get their results
result = executor.run_and_wait([instance_future1, instance_future2])
print(f"Class instance result:{result}")
# The main program continues immediately without waiting for test_function to complete.
print("Continuing after class methods...")
print() # Print empty


@executor.async_null_result
def test_function1(a,b):
    print(f"test_function1 async_data_handler")
    sleep(10)  # Simulate a time-consuming operation
    return a+b

@executor.async_null_result
def test_function2(a,b):
    print(f"test_function2 async_data_handler")
    sleep(1)  # Simulate a time-consuming operation
    return a+b

@executor.async_data_handler
def test_function3(a,b):
    print(f"test_function3 async_data_handler")
    sleep(15)  # Simulate a time-consuming operation
    return a+b

@executor.async_data_handler
def test_function4(a,b):
    print(f"test_function4 async_data_handler")
    sleep(4)  # Simulate a time-consuming operation
    return a+b


test_function1(10, 10)
test_function2(20, 20)
print("Continuing after fuction call with async_null_result...")

# Submit tasks to the executor
future3 = test_function3(30, 30)
future4 = test_function4(40, 40)

# Wait for all submitted tasks to complete and get their results
result = executor.run_and_wait([future3, future4])
print(result)

# This must be added to release resouces.
executor.shutdown()

License
This project is licensed under the MIT License. See the LICENSE file for details.

Copy code
This markdown file serves as a concise guide for users interested in leveraging the PyThreadFuture class for asynchronous task execution. It outlines the features, usage instructions, and provides an example for better understanding. Additionally, it includes licensing information for clarity on usage rights.
